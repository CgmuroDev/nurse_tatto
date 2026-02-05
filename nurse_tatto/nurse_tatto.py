import reflex as rx
import reflex.components.radix.themes as themes


class State(rx.State):
    pass


def navbar():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading("LAHAMY", size="8", color="white", font_weight="bold",
                          letter_spacing="wider", font_family="serif"),
                rx.spacer(),
                rx.hstack(
                    rx.link("INICIO", href="#home", color="white",
                           _hover={"color": "#8B0000", "transform": "translateY(-2px)"},
                           font_weight="500", transition="all 0.3s ease"),
                    rx.link("PORTAFOLIO", href="#portfolio", color="white",
                           _hover={"color": "#8B0000", "transform": "translateY(-2px)"},
                           font_weight="500", transition="all 0.3s ease"),
                    rx.link("ESTILOS", href="#styles", color="white",
                           _hover={"color": "#8B0000", "transform": "translateY(-2px)"},
                           font_weight="500", transition="all 0.3s ease"),
                    rx.link("ACERCA", href="#about", color="white",
                           _hover={"color": "#8B0000", "transform": "translateY(-2px)"},
                           font_weight="500", transition="all 0.3s ease"),
                    rx.link("CONTACTO", href="#contact", color="white",
                           _hover={"color": "#8B0000", "transform": "translateY(-2px)"},
                           font_weight="500", transition="all 0.3s ease"),
                    spacing="8",
                ),
                justify="between",
                align_items="center",
                padding_x="2rem",
                padding_y="1.5rem",
                width="100%",
            ),
            width="100%",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.heading("LAHAMY", size="6", color="white", font_weight="bold",
                          letter_spacing="wider", font_family="serif"),
                rx.spacer(),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon(tag="menu", size=24),
                            variant="ghost",
                            color="white",
                        ),
                    ),
                    rx.menu.content(
                        rx.menu.item("INICIO", href="#home"),
                        rx.menu.item("PORTAFOLIO", href="#portfolio"),
                        rx.menu.item("ESTILOS", href="#styles"),
                        rx.menu.item("ACERCA", href="#about"),
                        rx.menu.item("CONTACTO", href="#contact"),
                    ),
                ),
                justify="between",
                align_items="center",
                padding_x="1rem",
                padding_y="1rem",
            ),
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="1000",
        background_color="rgba(10, 10, 10, 0.95)",
        backdrop_filter="blur(10px)",
        border_bottom="1px solid #2a2a2a",
    )


def hero_section():
    return rx.section(
        rx.center(
            rx.vstack(
                rx.heading(
                    "LAHAMY",
                    size="9",
                    color="white",
                    font_weight="black",
                    letter_spacing="widest",
                    font_family="serif",
                    text_align="center",
                    margin_bottom="1rem",
                    animation="fadeInUp 1s ease-out",
                ),
                rx.heading(
                    "TATTOO ARTIST",
                    size="6",
                    color="#8B0000",
                    font_weight="medium",
                    letter_spacing="wide",
                    text_transform="uppercase",
                    text_align="center",
                    margin_bottom="2rem",
                    animation="fadeInUp 1s ease-out 0.2s both",
                ),
                rx.text(
                    "Arte gótico en tu piel • Expresión oscura y única",
                    size="5",
                    color="#c0c0c0",
                    text_align="center",
                    line_height="1.6",
                    margin_bottom="3rem",
                    animation="fadeInUp 1s ease-out 0.4s both",
                ),
                rx.hstack(
                    rx.button(
                        "VER PORTAFOLIO",
                        on_click=rx.scroll_to("portfolio"),
                        display="inline-flex",
                        align_items="center",
                        justify_content="center",
                        background_color="#8B0000",
                        color="white",
                        font_weight="600",
                        padding_x="2.5rem",
                        padding_y="1.25rem",
                        border_radius="12px",
                        cursor="pointer",
                        border="2px solid transparent",
                        animation="fadeInUp 1s ease-out 0.6s both",
                        transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                        _hover={
                            "background_color": "#690000",
                            "transform": "translateY(-2px) scale(1.05)",
                            "box_shadow": "0 15px 30px rgba(139, 0, 0, 0.4)"
                        },
                    ),
                    rx.button(
                        "CONTACTAR",
                        on_click=rx.scroll_to("contact"),
                        display="inline-flex",
                        align_items="center",
                        justify_content="center",
                        background_color="transparent",
                        color="white",
                        border="2px solid white",
                        font_weight="600",
                        padding_x="2.5rem",
                        padding_y="1.25rem",
                        border_radius="12px",
                        cursor="pointer",
                        animation="fadeInUp 1s ease-out 0.8s both",
                        transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                        _hover={
                            "background_color": "white",
                            "color": "black",
                            "transform": "translateY(-2px) scale(1.05)",
                            "box_shadow": "0 15px 30px rgba(255, 255, 255, 0.2)"
                        },
                    ),
                    spacing="4",
                    align_items="center",
                    justify_content="center",
                    width="100%",
                ),
                spacing="8",
                align_items="center",
                min_height="80vh",
                width="100%",
                justify_content="center",
                position="relative",
                z_index="10",
            ),
            width="100%",
        ),
        id="home",
        position="relative",
        padding_top="5rem",
        width="100%",
        overflow="hidden",
        style={
            "background": "linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%)",
            "position": "relative",
            "&::before": {
                "content": "''",
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
                "background": "radial-gradient(circle at 20% 50%, rgba(139, 0, 0, 0.1) 0%, transparent 50%)",
                "animation": "float 6s ease-in-out infinite",
                "pointer-events": "none",
            },
            "&::after": {
                "content": "''",
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
                "background": "radial-gradient(circle at 80% 80%, rgba(139, 0, 0, 0.05) 0%, transparent 50%)",
                "animation": "float 8s ease-in-out infinite reverse",
                "pointer-events": "none",
            }
        }
    )


def portfolio_gallery():
    portfolio_items = [
        {"title": "Gothic Rose", "category": "Dark/Gothic"},
        {"title": "Skull Design", "category": "Traditional"},
        {"title": "Geometric Wolf", "category": "Minimalist"},
        {"title": "Dark Portrait", "category": "Black & Grey"},
        {"title": "Ornamental Cross", "category": "Dark/Gothic"},
        {"title": "Minimal Lines", "category": "Minimalist"},
    ]

    return rx.section(
        rx.box(
            rx.vstack(
                rx.box(
                    height="1px",
                    width="80px",
                    background_color="#8B0000",
                    margin_bottom="1.5rem",
                ),
                rx.heading(
                    "PORTAFOLIO",
                    size="9",
                    color="white",
                    font_weight="black",
                    letter_spacing="wide",
                    text_align="center",
                    margin_bottom="1rem",
                ),
                rx.text(
                    "Explora mi colección de arte oscuro en la piel",
                    size="5",
                    color="#c0c0c0",
                    text_align="center",
                    margin_bottom="4rem",
                ),
                spacing="0",
                align_items="center",
                width="100%",
            ),
            rx.grid(
                rx.foreach(
                    portfolio_items,
                    lambda item: rx.card(
                        rx.vstack(
                            rx.box(
                                width="100%",
                                height="300px",
                                background="linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%)",
                                border_radius="16px",
                                margin_bottom="1rem",
                                position="relative",
                                overflow="hidden",
                                style={
                                    "&::after": {
                                        "content": "''",
                                        "position": "absolute",
                                        "top": "0",
                                        "left": "0",
                                        "right": "0",
                                        "bottom": "0",
                                        "background": "radial-gradient(circle at center, rgba(139, 0, 0, 0.15) 0%, transparent 70%)",
                                    }
                                },
                            ),
                            rx.heading(
                                item["title"],
                                size="5",
                                color="white",
                                font_weight="600",
                                margin_bottom="0.5rem",
                            ),
                            rx.badge(
                                item["category"],
                                color_scheme="red",
                                variant="solid",
                                size="2",
                                border_radius="8px",
                            ),
                            spacing="3",
                            padding="1.5rem",
                            align_items="flex-start",
                            width="100%",
                        ),
                        background_color="#1a1a1a",
                        border="1px solid #2a2a2a",
                        border_radius="20px",
                        _hover={
                            "transform": "translateY(-10px) scale(1.02)",
                            "box_shadow": "0 30px 60px rgba(139, 0, 0, 0.5)",
                            "border_color": "#8B0000"
                        },
                        transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                        cursor="pointer",
                        overflow="hidden",
                    ),
                ),
                columns=rx.breakpoints(initial="1", sm="2", lg="3"),
                spacing="6",
                width="100%",
            ),
            padding_x="2rem",
            padding_y="5rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="portfolio",
        background_color="#0a0a0a",
        width="100%",
    )


def styles_section():
    styles = [
        {"name": "Black & Grey", "description": "Monochromas profundas con sombras detalladas", "icon": "●"},
        {"name": "Dark/Gothic", "description": "Arte oscuro con elementos góticos y simbólicos", "icon": "†"},
        {"name": "Traditional", "description": "Estilo clásico con líneas gruesas y colores vibrantes", "icon": "▲"},
        {"name": "Minimalist", "description": "Diseños simples y elegantes con líneas finas", "icon": "─"},
    ]

    return rx.section(
        rx.box(
            rx.vstack(
                rx.box(
                    height="1px",
                    width="80px",
                    background_color="#8B0000",
                    margin_bottom="1.5rem",
                ),
                rx.heading(
                    "ESTILOS DE TATUAJE",
                    size="9",
                    color="white",
                    font_weight="black",
                    letter_spacing="wide",
                    text_align="center",
                    margin_bottom="1rem",
                ),
                rx.text(
                    "Especializada en arte oscuro y expresivo",
                    size="5",
                    color="#c0c0c0",
                    text_align="center",
                    margin_bottom="4rem",
                ),
                spacing="0",
                align_items="center",
                width="100%",
            ),
            rx.grid(
                rx.foreach(
                    styles,
                    lambda style: rx.card(
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    style["icon"],
                                    size="9",
                                    color="#8B0000",
                                    text_align="center",
                                ),
                                margin_bottom="1.5rem",
                                padding="1rem",
                                background="radial-gradient(circle, rgba(139, 0, 0, 0.1) 0%, transparent 70%)",
                                border_radius="50%",
                                width="80px",
                                height="80px",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                            ),
                            rx.heading(
                                style["name"],
                                size="6",
                                color="white",
                                font_weight="700",
                                text_align="center",
                                margin_bottom="1rem",
                            ),
                            rx.text(
                                style["description"],
                                size="4",
                                color="#c0c0c0",
                                text_align="center",
                                line_height="1.8",
                            ),
                            spacing="2",
                            padding="2.5rem",
                            align_items="center",
                        ),
                        background="linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%)",
                        border="1px solid #2a2a2a",
                        border_radius="20px",
                        _hover={
                            "background": "linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%)",
                            "border_color": "#8B0000",
                            "transform": "translateY(-8px) scale(1.03)",
                            "box_shadow": "0 20px 40px rgba(139, 0, 0, 0.3)"
                        },
                        transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                    ),
                ),
                columns=rx.breakpoints(initial="1", sm="2", md="2", lg="4"),
                spacing="6",
                width="100%",
            ),
            padding_x="2rem",
            padding_y="5rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="styles",
        background="linear-gradient(180deg, #0a0a0a 0%, #0f0f0f 50%, #0a0a0a 100%)",
        width="100%",
    )


def about_section():
    return rx.section(
        rx.box(
            rx.vstack(
                rx.box(
                    height="1px",
                    width="80px",
                    background_color="#8B0000",
                    margin_bottom="1.5rem",
                ),
                rx.heading(
                    "ACERCA DE MI",
                    size="9",
                    color="white",
                    font_weight="black",
                    letter_spacing="wide",
                    text_align="center",
                    margin_bottom="4rem",
                ),
                spacing="0",
                align_items="center",
                width="100%",
            ),
            rx.grid(
                rx.vstack(
                    rx.text(
                        "Lahamy es una artista del tatuaje especializada en expresiones oscuras y únicas. Mi enfoque combina técnicas tradicionales con estética gótica moderna, creando piezas que son tanto atemporales como rebeldes.",
                        size="5",
                        color="#c0c0c0",
                        line_height="2",
                        margin_bottom="2rem",
                    ),
                    rx.text(
                        "Cada tatuaje es una obra de arte personalizada, diseñada para reflejar la individualidad y la historia de cada cliente. Desde intrincados diseños góticos hasta piezas minimalistas elegantes, mi trabajo busca capturar la esencia del arte oscuro en la piel.",
                        size="5",
                        color="#c0c0c0",
                        line_height="2",
                        margin_bottom="3rem",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="award", color="#8B0000", size=24),
                                background="rgba(139, 0, 0, 0.1)",
                                padding="0.75rem",
                                border_radius="8px",
                            ),
                            rx.text("5+ años de experiencia", color="white", font_weight="500", size="4"),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="users", color="#8B0000", size=24),
                                background="rgba(139, 0, 0, 0.1)",
                                padding="0.75rem",
                                border_radius="8px",
                            ),
                            rx.text("500+ clientes satisfechos", color="white", font_weight="500", size="4"),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="palette", color="#8B0000", size=24),
                                background="rgba(139, 0, 0, 0.1)",
                                padding="0.75rem",
                                border_radius="8px",
                            ),
                            rx.text("Especialista en arte oscuro", color="white", font_weight="500", size="4"),
                            spacing="3",
                            align_items="center",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    align_items="flex-start",
                ),
                rx.box(
                    width="100%",
                    height="600px",
                    background="linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%)",
                    border="2px solid #2a2a2a",
                    border_radius="24px",
                    position="relative",
                    overflow="hidden",
                    style={
                        "&::after": {
                            "content": "''",
                            "position": "absolute",
                            "top": "50%",
                            "left": "50%",
                            "transform": "translate(-50%, -50%)",
                            "width": "200px",
                            "height": "200px",
                            "background": "radial-gradient(circle, rgba(139, 0, 0, 0.2) 0%, transparent 70%)",
                        }
                    },
                ),
                columns=rx.breakpoints(initial="1", lg="2"),
                spacing="9",
                align_items="center",
            ),
            padding_x="2rem",
            padding_y="5rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="about",
        background_color="#0a0a0a",
        width="100%",
    )


def contact_section():
    return rx.section(
        rx.box(
            rx.vstack(
                rx.box(
                    height="1px",
                    width="80px",
                    background_color="#8B0000",
                    margin_bottom="1.5rem",
                ),
                rx.heading(
                    "CONTACTO",
                    size="9",
                    color="white",
                    font_weight="black",
                    letter_spacing="wide",
                    text_align="center",
                    margin_bottom="1rem",
                ),
                rx.text(
                    "¿Lista para llevar arte oscuro a tu piel? Contáctame para consultar disponibilidad y cotizaciones.",
                    size="5",
                    color="#c0c0c0",
                    text_align="center",
                    line_height="1.8",
                    margin_bottom="4rem",
                    max_width="700px",
                ),
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.box(
                                rx.icon(tag="message-circle", color="#8B0000", size=36),
                                background="rgba(139, 0, 0, 0.1)",
                                padding="1rem",
                                border_radius="16px",
                                margin_bottom="1.5rem",
                            ),
                            rx.heading("Facebook", size="6", color="white", font_weight="700", margin_bottom="0.75rem"),
                            rx.text("Sígueme en Facebook para ver mi trabajo reciente", color="#c0c0c0", text_align="center", line_height="1.6", margin_bottom="1.5rem"),
                            rx.link(
                                rx.button("Visitar Facebook", variant="outline", color="white", border_color="#8B0000", border_width="2px", border_radius="10px", padding_x="1.5rem", padding_y="0.75rem"),
                                href="https://facebook.com",
                                is_external=True,
                            ),
                            spacing="0",
                            padding="2.5rem",
                            align_items="center",
                        ),
                        background="linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%)",
                        border="1px solid #2a2a2a",
                        border_radius="20px",
                        _hover={
                            "border_color": "#8B0000",
                            "transform": "translateY(-8px)",
                            "box_shadow": "0 20px 40px rgba(139, 0, 0, 0.3)"
                        },
                        transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.box(
                                rx.icon(tag="calendar", color="#8B0000", size=36),
                                background="rgba(139, 0, 0, 0.1)",
                                padding="1rem",
                                border_radius="16px",
                                margin_bottom="1.5rem",
                            ),
                            rx.heading("Reservar Cita", size="6", color="white", font_weight="700", margin_bottom="0.75rem"),
                            rx.text("Agenda tu sesión para una consulta personalizada", color="#c0c0c0", text_align="center", line_height="1.6", margin_bottom="1.5rem"),
                            rx.button(
                                "Contactar Ahora",
                                background_color="#8B0000",
                                color="white",
                                border_radius="10px",
                                padding_x="1.5rem",
                                padding_y="0.75rem",
                                _hover={"background_color": "#690000", "transform": "scale(1.05)"},
                                transition="all 0.3s ease",
                            ),
                            spacing="0",
                            padding="2.5rem",
                            align_items="center",
                        ),
                        background="linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%)",
                        border="1px solid #2a2a2a",
                        border_radius="20px",
                        _hover={
                            "border_color": "#8B0000",
                            "transform": "translateY(-8px)",
                            "box_shadow": "0 20px 40px rgba(139, 0, 0, 0.3)"
                        },
                        transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                    ),
                    columns=rx.breakpoints(initial="1", sm="2"),
                    spacing="6",
                    width="100%",
                    max_width="800px",
                ),
                rx.text(
                    "Tiempo de respuesta: 24-48 horas",
                    size="4",
                    color="#666",
                    text_align="center",
                    margin_top="3rem",
                ),
                align_items="center",
                min_height="80vh",
            ),
            padding_x="2rem",
            padding_y="5rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="contact",
        background="linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%)",
        width="100%",
    )


def footer():
    return rx.box(
        rx.box(
            rx.hstack(
                rx.heading("LAHAMY", size="6", color="white", font_weight="bold",
                          letter_spacing="wider", font_family="serif"),
                rx.spacer(),
                rx.text("© 2024 Lahamy Tattoo. Todos los derechos reservados.", color="#666"),
                spacing="4",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
        ),
        padding_y="2rem",
        border_top="1px solid #2a2a2a",
        background_color="#0a0a0a",
        width="100%",
    )


def index():
    return rx.vstack(
        navbar(),
        hero_section(),
        portfolio_gallery(),
        styles_section(),
        about_section(),
        contact_section(),
        footer(),
        width="100%",
        min_height="100vh",
        background_color="#0a0a0a",
        spacing="0",
        style={"scroll-behavior": "smooth"},
    )


app = rx.App(
    theme=themes.theme(
        appearance="dark",
        accent_color="red",
        gray_color="mauve",
        radius="large",
        scaling="100%",
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap",
        "animations.css"
    ],
    style={
        "scroll-behavior": "smooth",
        "scroll-padding-top": "100px",  # Aumenta el padding para mejor visual
    },
)

app.add_page(index)
