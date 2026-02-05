import reflex as rx

config = rx.Config(
    app_name="nurse_tatto",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)