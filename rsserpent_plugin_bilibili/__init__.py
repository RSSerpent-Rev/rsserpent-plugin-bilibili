from rsserpent_rev.models import Persona, Plugin

from . import app, user

plugin = Plugin(
    name="rsserpent-plugin-bilibili",
    author=Persona(
        name="creedowl",
        link="https://github.com/creedowl",
        email="creedowl@gmail.com",
    ),
    prefix="/bilibili",
    repository="https://github.com/RSSerpent-Rev/rsserpent-plugin-bilibili",
    routers={
        user.video.path: user.video.provider,
        user.bangumi.path: user.bangumi.provider,
        user.cinema.path: user.cinema.provider,
        app.update.path: app.update.provider,
    },
)
