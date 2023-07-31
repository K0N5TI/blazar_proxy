"""
This is the first version of the Blazar Proxy API
"""
from flask import Blueprint, jsonify, request, url_for
import pandas as pd
from ...model import Cat, Vertice, db

bp = Blueprint("v1", __name__, url_prefix="/v1")

@bp.route("/")
def v1_info():
    """
    Index page for the v1 API
    Returns:
        JSON: JSON response with API information
    """
    return {
        "version": "1.0",
        "description": "This is the first version of the Blazar Proxy API",
        "endpoints": {
            "cats": "/cats",
            "vertices": "/vertices"
        },
    }


def paginate_and_filter(column):
    """
    Paginate and filter a SQLAlchemy query
    """
    query = db.select(column)

    page = db.paginate(
        query,
        page=request.args.get("page", 1, type=int),
        per_page=request.args.get("per_page", 10, type=int),
        max_per_page=100,
        error_out=True,
        count=True,
    )
    items_query = (
        db.select(column).offset((page.page - 1) * page.per_page).limit(page.per_page)
    )
    query_result = pd.read_sql(items_query, db.engine)

    return {
        "page": page.page,
        "per_page": page.per_page,
        "items": query_result.to_dict(orient="records"),
        "total": page.total,
        "first": page.first,
        "last": page.last,
        "pages": page.pages,
        "has_prev": page.has_prev,
        "prev_num": page.prev_num,
        "has_next": page.has_next,
        "next_num": page.next_num,
        "next": url_for(
            request.endpoint,
            page=page.next_num,
            per_page=page.per_page,
        ),
        "prev": url_for(
            request.endpoint,
            page=page.prev_num,
            per_page=page.per_page,
        ),
    }


@bp.route("/cats")
def cats():
    """
    CATs endpoint
    Returns:
        JSON: JSON response with CATs
        Pagination information
    """
    return jsonify(paginate_and_filter(column=Cat))


@bp.route("/vertices")
def vertices():
    """
    Vertices endpoint
    Returns:
        JSON: JSON response with vertices
        Pagination information
    """
    return jsonify(paginate_and_filter(column=Vertice))
