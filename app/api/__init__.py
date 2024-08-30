from flask import Flask
from .database import initialize_db

def create_app():
    app = Flask(__name__)

    # データベースの初期化
    initialize_db(app)

    # 他のブループリントや設定の登録
    # ユーザー情報に関するAPI
    from .view.user_view.user_select import user_select
    from .view.user_view.user_insert import user_insert
    from .view.user_view.user_update import user_update
    from .view.user_view.user_delete import user_delete

    app.register_blueprint(user_select, url_prefix="/api/user/select")
    app.register_blueprint(user_insert, url_prefix="/api/user/insert")
    app.register_blueprint(user_update, url_prefix="/api/user/update")
    app.register_blueprint(user_delete, url_prefix="/api/user/delete")

    # タグ情報に関するAPI
    from .view.tag_view.tags_find import tags_find

    app.register_blueprint(tags_find, url_prefix="/api/tags/find")

    return app

# app = create_app()