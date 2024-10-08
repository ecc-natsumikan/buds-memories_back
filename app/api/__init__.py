from flask import Flask
from .database import initialize_db

def create_app():
    app = Flask(__name__)

    # データベースの初期化
    initialize_db(app)

    # 他のブループリントや設定の登録
    # ユーザー情報に関するAPI
    from .view.user_view.user_find import user_find
    from .view.user_view.user_insert import user_insert
    from .view.user_view.user_update import user_update
    from .view.user_view.user_delete import user_delete

    app.register_blueprint(user_find, url_prefix="/api/user/find")
    app.register_blueprint(user_insert, url_prefix="/api/user/insert")
    app.register_blueprint(user_update, url_prefix="/api/user/update")
    app.register_blueprint(user_delete, url_prefix="/api/user/delete")

    # タグ情報に関するAPI
    from .view.tag_view.tags_find import tags_find

    app.register_blueprint(tags_find, url_prefix="/api/tags/find")

    # 投稿情報に関するAPI
    from .view.post_view.posts_insert import posts_insert
    from .view.post_view.posts_delete import posts_delete
    from .view.post_view.find.user_posts import user_posts_find
    from .view.post_view.find.user_tag_posts import user_tag_posts_find
    from .view.post_view.find.user_tag_posts_growth_period import user_tag_posts_growth_period_find
    from .view.post_view.find.tag_posts import tag_posts_find
    from .view.post_view.find.tag_posts_growth_period import tag_posts_growth_period_find
    from .view.post_view.find.tag_posts_growth_period_count import tag_posts_growth_period_count_find
    from .view.post_view.like_posts_update import like_post_update
    from .view.post_view.like_posts_find import like_posts_find
    from .view.post_view.posts_like_delete import posts_like_delete


    app.register_blueprint(posts_insert, url_prefix="/api/posts/insert")
    app.register_blueprint(posts_delete, url_prefix="/api/posts/delete")
    app.register_blueprint(user_posts_find, url_prefix="/api/posts/find/user")
    app.register_blueprint(user_tag_posts_find, url_prefix="/api/posts/find/user/tag")
    app.register_blueprint(user_tag_posts_growth_period_find, url_prefix="/api/posts/find/user/tag/growth-period")
    app.register_blueprint(tag_posts_find, url_prefix="/api/posts/find/tag")
    app.register_blueprint(tag_posts_growth_period_find, url_prefix="/api/posts/find/tag/growth-period")
    app.register_blueprint(tag_posts_growth_period_count_find, url_prefix="/api/posts/find/tag/growth-period/count")
    app.register_blueprint(like_post_update, url_prefix="/api/posts/like/update")
    app.register_blueprint(like_posts_find, url_prefix="/api/posts/like/find")
    app.register_blueprint(posts_like_delete, url_prefix="/api/posts/like/delete")

    # 育成アイテムに関するAPI
    from .view.grow_item_view.grow_item_find import grow_item_find
    from .view.grow_item_view.grow_item_stage_check_update_find import grow_item_stage_check_update_find

    app.register_blueprint(grow_item_find, url_prefix="/api/grow-item/find")
    app.register_blueprint(grow_item_stage_check_update_find, url_prefix="/api/grow-item/stage/check/update")

    return app
