import reflex as rx
import reflex.components.radix.themes as themes
import json


# ─── State with real functionality ───────────────────────────────────
class State(rx.State):
    # Portfolio filter
    active_filter: str = "Todos"
    
    # Contact form
    contact_name: str = ""
    contact_email: str = ""
    contact_message: str = ""
    form_submitted: bool = False
    
    # Mobile menu
    menu_open: bool = False

    @rx.event
    def set_filter(self, category: str):
        self.active_filter = category

    @rx.event
    def toggle_menu(self):
        self.menu_open = not self.menu_open

    @rx.event
    def handle_submit(self):
        if self.contact_name and self.contact_message:
            # Escapar valores para JavaScript
            name = json.dumps(self.contact_name)
            email = json.dumps(self.contact_email)
            message = json.dumps(self.contact_message)
            
            # Marcar como enviado inmediatamente para mostrar el estado de carga
            self.form_submitted = True
            
            return rx.call_script(
                f"""
                emailjs.send('service_z49ntj4', 'template_psaseu4', {{
                    name: {name},
                    email: {email},
                    message: {message}
                }}).then(function(response) {{
                    console.log('Email enviado correctamente', response);
                }}).catch(function(error) {{
                    console.error('Error al enviar:', error);
                    alert('Error al enviar el mensaje: ' + JSON.stringify(error));
                }});
                """
            )

    @rx.event
    def mark_submitted(self):
        self.form_submitted = True

    @rx.event
    def reset_form(self):
        self.contact_name = ""
        self.contact_email = ""
        self.contact_message = ""
        self.form_submitted = False

    @rx.var
    def filtered_portfolio(self) -> list[dict]:
        items = [
            {"title": "Gothic Rose", "category": "Dark/Gothic", "desc": "Rosa envuelta en espinas con sombras profundas"},
            {"title": "Skull Design", "category": "Traditional", "desc": "Calavera clásica con detalles ornamentales"},
            {"title": "Geometric Wolf", "category": "Minimalist", "desc": "Lobo en trazos geométricos precisos"},
            {"title": "Dark Portrait", "category": "Black & Grey", "desc": "Retrato sombrío con técnica realista"},
            {"title": "Ornamental Cross", "category": "Dark/Gothic", "desc": "Cruz ornamental con filigrana oscura"},
            {"title": "Minimal Lines", "category": "Minimalist", "desc": "Líneas finas con composición elegante"},
            {"title": "Sacred Heart", "category": "Traditional", "desc": "Corazón sagrado con llamas y espinas"},
            {"title": "Raven Silhouette", "category": "Black & Grey", "desc": "Cuervo en vuelo con degradados suaves"},
            {"title": "Death Moth", "category": "Dark/Gothic", "desc": "Polilla de la muerte con mandala"},
        ]
        if self.active_filter == "Todos":
            return items
        return [i for i in items if i["category"] == self.active_filter]


# ─── Components ──────────────────────────────────────────────────────

def section_header(title: str, subtitle: str = ""):
    return rx.vstack(
        rx.box(height="2px", width="60px", background="linear-gradient(90deg, #8B0000, #cc0000)"),
        rx.heading(
            title,
            size="8",
            color="white",
            font_weight="900",
            letter_spacing="0.15em",
            font_family="'Playfair Display', serif",
            text_align="center",
        ),
        rx.cond(
            subtitle != "",
            rx.text(
                subtitle,
                size="4",
                color="#888",
                text_align="center",
                line_height="1.8",
                max_width="600px",
                font_family="'Inter', sans-serif",
            ),
            rx.fragment(),
        ),
        spacing="4",
        align_items="center",
        width="100%",
        margin_bottom="3rem",
        class_name="fade-in-up",
    )


def navbar():
    nav_links = [
        ("INICIO", "#home"),
        ("PORTAFOLIO", "#portfolio"),
        ("ESTILOS", "#styles"),
        ("ACERCA", "#about"),
        ("TESTIMONIOS", "#testimonials"),
        ("CONTACTO", "#contact"),
    ]
    return rx.box(
        # Desktop
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.box(
                        width="8px",
                        height="8px",
                        background="#8B0000",
                        border_radius="50%",
                        box_shadow="0 0 10px rgba(139,0,0,0.6)",
                    ),
                    rx.heading(
                        "NURSE TATTO",
                        size="7",
                        color="white",
                        font_weight="900",
                        letter_spacing="0.2em",
                        font_family="'Playfair Display', serif",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                rx.spacer(),
                rx.hstack(
                    *[
                        rx.link(
                            text,
                            href=href,
                            color="#aaa",
                            font_size="0.75rem",
                            font_weight="600",
                            letter_spacing="0.15em",
                            font_family="'Inter', sans-serif",
                            _hover={"color": "#fff", "text_decoration": "none"},
                            transition="color 0.3s ease",
                            text_decoration="none",
                        )
                        for text, href in nav_links
                    ],
                    spacing="7",
                ),
                justify="between",
                align_items="center",
                padding_x="3rem",
                padding_y="1.25rem",
                width="100%",
                max_width="1400px",
                margin="0 auto",
            ),
            width="100%",
        ),
        # Mobile
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.box(
                        width="6px",
                        height="6px",
                        background="#8B0000",
                        border_radius="50%",
                    ),
                    rx.heading(
                        "NURSE TATTO",
                        size="5",
                        color="white",
                        font_weight="900",
                        letter_spacing="0.2em",
                        font_family="'Playfair Display', serif",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                rx.spacer(),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon(tag="menu", size=22, color="white"),
                            variant="ghost",
                            cursor="pointer",
                        ),
                    ),
                    rx.menu.content(
                        *[
                            rx.menu.item(
                                rx.link(text, href=href, color="inherit", text_decoration="none", width="100%"),
                            )
                            for text, href in nav_links
                        ],
                        background="#1a1a1a",
                        border="1px solid #333",
                    ),
                ),
                justify="between",
                align_items="center",
                padding_x="1.25rem",
                padding_y="1rem",
            ),
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="1000",
        background="rgba(8, 8, 8, 0.92)",
        backdrop_filter="blur(20px)",
        border_bottom="1px solid rgba(139, 0, 0, 0.15)",
    )


def hero_section():
    return rx.section(
        rx.center(
            rx.vstack(
                # Decorative top element
                rx.hstack(
                    rx.box(height="1px", width="40px", background="#8B0000"),
                    rx.text(
                        "TATTOO ARTISTRY",
                        font_size="0.65rem",
                        color="#8B0000",
                        letter_spacing="0.4em",
                        font_weight="600",
                        font_family="'Inter', sans-serif",
                    ),
                    rx.box(height="1px", width="40px", background="#8B0000"),
                    spacing="4",
                    align_items="center",
                    class_name="fade-in-up",
                ),
                # Main heading
                rx.heading(
                    "NURSE TATTO",
                    font_size=rx.breakpoints(initial="4rem", sm="6rem", md="8rem", lg="10rem"),
                    color="white",
                    font_weight="900",
                    letter_spacing="0.15em",
                    font_family="'Playfair Display', serif",
                    text_align="center",
                    line_height="0.9",
                    class_name="fade-in-up delay-1",
                    style={
                        "text_shadow": "0 0 80px rgba(139, 0, 0, 0.3)",
                    },
                ),
                # Subtitle
                rx.text(
                    "Arte oscuro y expresivo en tu piel",
                    font_size=rx.breakpoints(initial="1rem", md="1.25rem"),
                    color="#666",
                    text_align="center",
                    line_height="1.8",
                    font_family="'Inter', sans-serif",
                    font_weight="300",
                    letter_spacing="0.05em",
                    class_name="fade-in-up delay-2",
                ),
                # CTA buttons
                rx.hstack(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.text("VER PORTAFOLIO", font_size="0.75rem", letter_spacing="0.15em"),
                                rx.icon(tag="arrow-down", size=16),
                                spacing="2",
                                align_items="center",
                            ),
                            background="linear-gradient(135deg, #8B0000, #aa0000)",
                            color="white",
                            font_weight="600",
                            padding_x="2rem",
                            padding_y="1rem",
                            border_radius="0",
                            cursor="pointer",
                            border="none",
                            _hover={
                                "opacity": "0.85",
                                "transform": "translateY(-2px)",
                                "box_shadow": "0 20px 40px rgba(139, 0, 0, 0.4)",
                            },
                            transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                        ),
                        href="#portfolio",
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.button(
                            rx.text("CONTACTAR", font_size="0.75rem", letter_spacing="0.15em"),
                            background="transparent",
                            color="#aaa",
                            border="1px solid #333",
                            font_weight="600",
                            padding_x="2rem",
                            padding_y="1rem",
                            border_radius="0",
                            cursor="pointer",
                            _hover={
                                "color": "white",
                                "border_color": "#8B0000",
                                "transform": "translateY(-2px)",
                            },
                            transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                        ),
                        href="#contact",
                        text_decoration="none",
                    ),
                    spacing="4",
                    align_items="center",
                    justify_content="center",
                    class_name="fade-in-up delay-3",
                ),
                # Scroll indicator
                rx.box(
                    rx.vstack(
                        rx.box(
                            width="1px",
                            height="40px",
                            background="linear-gradient(to bottom, #8B0000, transparent)",
                            class_name="scroll-line",
                        ),
                        spacing="2",
                        align_items="center",
                    ),
                    position="absolute",
                    bottom="2rem",
                    left="50%",
                    transform="translateX(-50%)",
                    class_name="fade-in-up delay-4",
                ),
                spacing="6",
                align_items="center",
                min_height="100vh",
                width="100%",
                justify_content="center",
                position="relative",
                z_index="10",
                padding_top="5rem",
            ),
            width="100%",
        ),
        id="home",
        position="relative",
        width="100%",
        overflow="hidden",
        background="#080808",
        style={
            "&::before": {
                "content": "''",
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
                "background": "radial-gradient(ellipse at 20% 50%, rgba(139, 0, 0, 0.06) 0%, transparent 60%)",
                "pointer_events": "none",
            },
            "&::after": {
                "content": "''",
                "position": "absolute",
                "top": "0",
                "left": "0",
                "right": "0",
                "bottom": "0",
                "background_image": "radial-gradient(rgba(255,255,255,0.02) 1px, transparent 1px)",
                "background_size": "40px 40px",
                "pointer_events": "none",
            },
        },
    )


def portfolio_card(item: dict):
    return rx.box(
        rx.vstack(
            # Image placeholder with overlay
            rx.box(
                rx.center(
                    rx.icon(tag="image", size=32, color="#333"),
                    width="100%",
                    height="100%",
                ),
                # Hover overlay
                rx.box(
                    rx.vstack(
                        rx.icon(tag="expand", size=24, color="white"),
                        rx.text(
                            "Ver detalle",
                            color="white",
                            font_size="0.75rem",
                            letter_spacing="0.1em",
                            font_family="'Inter', sans-serif",
                        ),
                        spacing="2",
                        align_items="center",
                        justify_content="center",
                        height="100%",
                        width="100%",
                    ),
                    position="absolute",
                    top="0",
                    left="0",
                    right="0",
                    bottom="0",
                    background="rgba(139, 0, 0, 0.7)",
                    opacity="0",
                    _group_hover={"opacity": "1"},
                    transition="opacity 0.4s ease",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                width="100%",
                height="280px",
                background="linear-gradient(145deg, #1a1a1a, #111)",
                position="relative",
                overflow="hidden",
            ),
            # Info
            rx.vstack(
                rx.text(
                    item["title"],
                    color="white",
                    font_weight="600",
                    font_size="1rem",
                    font_family="'Playfair Display', serif",
                ),
                rx.text(
                    item["desc"],
                    color="#666",
                    font_size="0.8rem",
                    line_height="1.5",
                    font_family="'Inter', sans-serif",
                ),
                rx.text(
                    item["category"],
                    color="#8B0000",
                    font_size="0.65rem",
                    letter_spacing="0.15em",
                    font_weight="600",
                    text_transform="uppercase",
                    font_family="'Inter', sans-serif",
                ),
                spacing="2",
                padding="1.25rem",
                align_items="flex-start",
                width="100%",
            ),
            spacing="0",
            width="100%",
        ),
        background="#111",
        border="1px solid #1a1a1a",
        overflow="hidden",
        cursor="pointer",
        _hover={
            "border_color": "rgba(139, 0, 0, 0.4)",
            "transform": "translateY(-6px)",
            "box_shadow": "0 20px 50px rgba(0, 0, 0, 0.5)",
        },
        transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
        role="group",
        class_name="fade-in-up",
    )


def portfolio_gallery():
    categories = ["Todos", "Dark/Gothic", "Black & Grey", "Traditional", "Minimalist"]

    return rx.section(
        rx.box(
            section_header("PORTAFOLIO", "Cada pieza es única — arte oscuro que cuenta tu historia"),
            # Filter buttons
            rx.hstack(
                *[
                    rx.button(
                        rx.text(cat, font_size="0.7rem", letter_spacing="0.1em"),
                        background=rx.cond(
                            State.active_filter == cat,
                            "#8B0000",
                            "transparent",
                        ),
                        color=rx.cond(
                            State.active_filter == cat,
                            "white",
                            "#666",
                        ),
                        border=rx.cond(
                            State.active_filter == cat,
                            "1px solid #8B0000",
                            "1px solid #333",
                        ),
                        padding_x="1.25rem",
                        padding_y="0.5rem",
                        border_radius="0",
                        cursor="pointer",
                        _hover={"color": "white", "border_color": "#8B0000"},
                        transition="all 0.3s ease",
                        on_click=State.set_filter(cat),
                    )
                    for cat in categories
                ],
                spacing="3",
                flex_wrap="wrap",
                justify_content="center",
                margin_bottom="3rem",
            ),
            # Grid
            rx.grid(
                rx.foreach(
                    State.filtered_portfolio,
                    portfolio_card,
                ),
                columns=rx.breakpoints(initial="1", sm="2", lg="3"),
                spacing="5",
                width="100%",
            ),
            padding_x=rx.breakpoints(initial="1rem", md="2rem"),
            padding_y="6rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="portfolio",
        background="#0a0a0a",
        width="100%",
    )


def style_card(name: str, description: str, icon_tag: str):
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(tag=icon_tag, color="#8B0000", size=28),
                padding="1rem",
                background="rgba(139, 0, 0, 0.08)",
                border="1px solid rgba(139, 0, 0, 0.15)",
            ),
            rx.text(
                name,
                color="white",
                font_weight="700",
                font_size="1.1rem",
                font_family="'Playfair Display', serif",
            ),
            rx.text(
                description,
                color="#666",
                font_size="0.85rem",
                line_height="1.7",
                font_family="'Inter', sans-serif",
            ),
            spacing="4",
            padding="2rem",
            align_items="flex-start",
        ),
        background="#111",
        border="1px solid #1a1a1a",
        _hover={
            "border_color": "rgba(139, 0, 0, 0.4)",
            "transform": "translateY(-4px)",
            "box_shadow": "0 15px 40px rgba(0, 0, 0, 0.4)",
        },
        transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
        class_name="fade-in-up",
    )


def styles_section():
    return rx.section(
        rx.box(
            section_header("ESTILOS", "Especializada en arte oscuro y expresivo"),
            rx.grid(
                style_card("Black & Grey", "Tonalidades monocromáticas con degradados profundos y sombras que crean dimensión y realismo.", "circle"),
                style_card("Dark / Gothic", "Elementos góticos, simbología oscura y motivos que evocan lo misterioso y lo eterno.", "skull"),
                style_card("Traditional", "Líneas gruesas y definidas con la fuerza del estilo clásico americano reinterpretado.", "flame"),
                style_card("Minimalist", "La belleza de lo simple — líneas finas y composiciones elegantes con espacio negativo.", "minus"),
                columns=rx.breakpoints(initial="1", sm="2", lg="4"),
                spacing="5",
                width="100%",
            ),
            padding_x=rx.breakpoints(initial="1rem", md="2rem"),
            padding_y="6rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="styles",
        background="#080808",
        width="100%",
        border_top="1px solid #1a1a1a",
        border_bottom="1px solid #1a1a1a",
    )


def stat_item(number: str, label: str):
    return rx.vstack(
        rx.text(
            number,
            font_size="2.5rem",
            font_weight="900",
            color="white",
            font_family="'Playfair Display', serif",
            line_height="1",
        ),
        rx.text(
            label,
            color="#666",
            font_size="0.75rem",
            letter_spacing="0.15em",
            text_transform="uppercase",
            font_family="'Inter', sans-serif",
        ),
        spacing="2",
        align_items="center",
    )


def about_section():
    return rx.section(
        rx.box(
            section_header("ACERCA DE MÍ"),
            rx.grid(
                # Text column
                rx.vstack(
                    rx.text(
                        "LaHamy es una artista del tatuaje especializada en expresiones oscuras y únicas. Mi enfoque combina técnicas tradicionales con estética gótica moderna, creando piezas que son tanto atemporales como rebeldes.",
                        color="#999",
                        font_size="1rem",
                        line_height="2",
                        font_family="'Inter', sans-serif",
                        font_weight="300",
                    ),
                    rx.text(
                        "Cada tatuaje es una obra de arte personalizada, diseñada para reflejar la individualidad y la historia de cada cliente. Desde intrincados diseños góticos hasta piezas minimalistas elegantes.",
                        color="#999",
                        font_size="1rem",
                        line_height="2",
                        font_family="'Inter', sans-serif",
                        font_weight="300",
                    ),
                    # Stats row
                    rx.hstack(
                        stat_item("5+", "Años"),
                        rx.box(width="1px", height="50px", background="#333"),
                        stat_item("500+", "Clientes"),
                        rx.box(width="1px", height="50px", background="#333"),
                        stat_item("1K+", "Tatuajes"),
                        spacing="6",
                        padding_top="2rem",
                        padding_bottom="2rem",
                        border_top="1px solid #1a1a1a",
                        margin_top="1rem",
                        width="100%",
                        justify_content="center",
                    ),
                    spacing="5",
                    align_items="flex-start",
                    class_name="fade-in-up",
                ),
                # Image column
                rx.box(
                    rx.image(
                        src="/imagenperfil.jpg",
                        width="100%",
                        height="100%",
                        object_fit="cover",
                        alt="LaHamy - Tattoo Artist",
                    ),
                    width="100%",
                    max_width="450px",
                    aspect_ratio="3/4",
                    overflow="hidden",
                    border="1px solid #1a1a1a",
                    class_name="fade-in-up delay-1",
                ),
                columns=rx.breakpoints(initial="1", lg="2"),
                spacing="8",
                align_items="center",
            ),
            padding_x=rx.breakpoints(initial="1rem", md="2rem"),
            padding_y="6rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="about",
        background="#0a0a0a",
        width="100%",
    )


def testimonial_card(name: str, text: str, style_type: str):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="quote", color="#8B0000", size=20),
                rx.spacer(),
                rx.text(style_type, color="#8B0000", font_size="0.65rem", letter_spacing="0.15em",
                        font_family="'Inter', sans-serif"),
                width="100%",
            ),
            rx.text(
                text,
                color="#999",
                font_size="0.9rem",
                line_height="1.8",
                font_style="italic",
                font_family="'Inter', sans-serif",
            ),
            rx.hstack(
                rx.box(width="20px", height="1px", background="#8B0000"),
                rx.text(name, color="white", font_weight="600", font_size="0.85rem",
                        font_family="'Playfair Display', serif"),
                spacing="3",
                align_items="center",
            ),
            spacing="5",
            padding="2rem",
        ),
        background="#111",
        border="1px solid #1a1a1a",
        _hover={"border_color": "rgba(139, 0, 0, 0.3)"},
        transition="border-color 0.3s ease",
        class_name="fade-in-up",
    )


def testimonials_section():
    return rx.section(
        rx.box(
            section_header("TESTIMONIOS", "Lo que dicen mis clientes"),
            rx.grid(
                testimonial_card(
                    "María G.",
                    "LaHamy capturó exactamente la visión que tenía en mente. El nivel de detalle en mi tatuaje gótico es increíble. Una verdadera artista.",
                    "DARK/GOTHIC",
                ),
                testimonial_card(
                    "Carlos R.",
                    "Profesional, limpia y con un talento único para el arte oscuro. Mi manga quedó mejor de lo que imaginé. Totalmente recomendada.",
                    "BLACK & GREY",
                ),
                testimonial_card(
                    "Ana L.",
                    "Buscaba algo minimalista pero con personalidad. LaHamy logró crear algo elegante y con mucho carácter. Volveré por más.",
                    "MINIMALIST",
                ),
                columns=rx.breakpoints(initial="1", md="3"),
                spacing="5",
                width="100%",
            ),
            padding_x=rx.breakpoints(initial="1rem", md="2rem"),
            padding_y="6rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="testimonials",
        background="#080808",
        border_top="1px solid #1a1a1a",
        width="100%",
    )


def contact_section():
    return rx.section(
        rx.box(
            section_header("CONTACTO", "¿Lista para llevar arte oscuro a tu piel?"),
            rx.grid(
                # Contact form
                rx.box(
                    rx.cond(
                        State.form_submitted,
                        # Success state
                        rx.vstack(
                            rx.icon(tag="check-circle", color="#8B0000", size=48),
                            rx.heading("¡Mensaje enviado!", size="5", color="white",
                                      font_family="'Playfair Display', serif"),
                            rx.text("Te responderé en 24-48 horas.", color="#666",
                                   font_family="'Inter', sans-serif"),
                            rx.button(
                                "Enviar otro mensaje",
                                on_click=State.reset_form,
                                background="transparent",
                                color="#8B0000",
                                border="1px solid #8B0000",
                                border_radius="0",
                                cursor="pointer",
                                padding_x="1.5rem",
                                padding_y="0.5rem",
                                _hover={"background": "#8B0000", "color": "white"},
                                transition="all 0.3s ease",
                            ),
                            spacing="4",
                            align_items="center",
                            justify_content="center",
                            min_height="400px",
                        ),
                        # Form
                        rx.vstack(
                            rx.text("ENVIAR MENSAJE", color="#666", font_size="0.7rem",
                                   letter_spacing="0.2em", font_family="'Inter', sans-serif",
                                   margin_bottom="1rem"),
                            rx.input(
                                placeholder="Tu nombre",
                                value=State.contact_name,
                                on_change=State.set_contact_name,
                                background="#111",
                                border="1px solid #222",
                                color="white",
                                padding="1rem",
                                border_radius="0",
                                width="100%",
                                height="48px",
                                font_size="16px",
                                font_family="'Inter', sans-serif",
                                _focus={"border_color": "#8B0000", "outline": "none"},
                                _placeholder={"color": "#444"},
                            ),
                            rx.input(
                                placeholder="Tu email",
                                value=State.contact_email,
                                on_change=State.set_contact_email,
                                background="#111",
                                border="1px solid #222",
                                color="white",
                                padding="1rem",
                                border_radius="0",
                                width="100%",
                                height="48px",
                                font_size="16px",
                                font_family="'Inter', sans-serif",
                                _focus={"border_color": "#8B0000", "outline": "none"},
                                _placeholder={"color": "#444"},
                            ),
                            rx.text_area(
                                placeholder="Describe tu idea de tatuaje...",
                                value=State.contact_message,
                                on_change=State.set_contact_message,
                                background="#111",
                                border="1px solid #222",
                                color="white",
                                padding="1rem",
                                border_radius="0",
                                width="100%",
                                min_height="150px",
                                font_size="16px",
                                font_family="'Inter', sans-serif",
                                _focus={"border_color": "#8B0000", "outline": "none"},
                                _placeholder={"color": "#444"},
                            ),
                            rx.button(
                                rx.hstack(
                                    rx.text("ENVIAR MENSAJE", font_size="0.85rem", letter_spacing="0.15em"),
                                    rx.icon(tag="send", size=18),
                                    spacing="3",
                                    align_items="center",
                                    justify_content="center",
                                    width="100%",
                                ),
                                type="button",
                                on_click=State.handle_submit,
                                background="linear-gradient(135deg, #8B0000, #aa0000)",
                                color="white",
                                font_weight="600",
                                padding_x="2rem",
                                padding_y="1.25rem",
                                border_radius="0",
                                cursor="pointer",
                                border="none",
                                width="100%",
                                min_height="52px",
                                _hover={
                                    "opacity": "0.85",
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "0 15px 30px rgba(139, 0, 0, 0.4)",
                                },
                                _active={
                                    "transform": "translateY(0)",
                                    "opacity": "0.7",
                                },
                                transition="all 0.3s ease",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                    ),
                    background="#0f0f0f",
                    border="1px solid #1a1a1a",
                    padding=rx.breakpoints(initial="1.25rem", md="2.5rem"),
                    class_name="fade-in-up",
                ),
                # Contact info & socials
                rx.vstack(
                    # WhatsApp card
                    rx.link(
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="message-circle", color="#25D366", size=24),
                                padding="0.75rem",
                                background="rgba(37, 211, 102, 0.1)",
                                border="1px solid rgba(37, 211, 102, 0.2)",
                            ),
                            rx.vstack(
                                rx.text("WhatsApp", color="white", font_weight="600",
                                       font_family="'Playfair Display', serif"),
                                rx.text("Mensaje directo", color="#666", font_size="0.8rem",
                                       font_family="'Inter', sans-serif"),
                                spacing="0",
                            ),
                            rx.spacer(),
                            rx.icon(tag="external-link", color="#444", size=16),
                            spacing="4",
                            align_items="center",
                            width="100%",
                            padding="1.25rem",
                        ),
                        href="https://wa.me/9981204933",
                        is_external=True,
                        text_decoration="none",
                        display="block",
                        width="100%",
                        background="#111",
                        border="1px solid #1a1a1a",
                        _hover={"border_color": "rgba(37, 211, 102, 0.4)"},
                        transition="border-color 0.3s ease",
                    ),
                    # Instagram card
                    rx.link(
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="camera", color="#E1306C", size=24),
                                padding="0.75rem",
                                background="rgba(225, 48, 108, 0.1)",
                                border="1px solid rgba(225, 48, 108, 0.2)",
                            ),
                            rx.vstack(
                                rx.text("Instagram", color="white", font_weight="600",
                                       font_family="'Playfair Display', serif"),
                                rx.text("@lahamy.ink", color="#666", font_size="0.8rem",
                                       font_family="'Inter', sans-serif"),
                                spacing="0",
                            ),
                            rx.spacer(),
                            rx.icon(tag="external-link", color="#444", size=16),
                            spacing="4",
                            align_items="center",
                            width="100%",
                            padding="1.25rem",
                        ),
                        href="https://instagram.com/lahamy.ink",
                        is_external=True,
                        text_decoration="none",
                        display="block",
                        width="100%",
                        background="#111",
                        border="1px solid #1a1a1a",
                        _hover={"border_color": "rgba(225, 48, 108, 0.4)"},
                        transition="border-color 0.3s ease",
                    ),
                    # Facebook card
                    rx.link(
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="globe", color="#1877F2", size=24),
                                padding="0.75rem",
                                background="rgba(24, 119, 242, 0.1)",
                                border="1px solid rgba(24, 119, 242, 0.2)",
                            ),
                            rx.vstack(
                                rx.text("Facebook", color="white", font_weight="600",
                                       font_family="'Playfair Display', serif"),
                                rx.text("Nurse Tatto", color="#666", font_size="0.8rem",
                                       font_family="'Inter', sans-serif"),
                                spacing="0",
                            ),
                            rx.spacer(),
                            rx.icon(tag="external-link", color="#444", size=16),
                            spacing="4",
                            align_items="center",
                            width="100%",
                            padding="1.25rem",
                        ),
                        href="https://facebook.com/lahamytattoo",
                        is_external=True,
                        text_decoration="none",
                        display="block",
                        width="100%",
                        background="#111",
                        border="1px solid #1a1a1a",
                        _hover={"border_color": "rgba(24, 119, 242, 0.4)"},
                        transition="border-color 0.3s ease",
                    ),
                    # Location
                    rx.box(
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="map-pin", color="#8B0000", size=24),
                                padding="0.75rem",
                                background="rgba(139, 0, 0, 0.1)",
                                border="1px solid rgba(139, 0, 0, 0.15)",
                            ),
                            rx.vstack(
                                rx.text("Ubicación", color="white", font_weight="600",
                                       font_family="'Playfair Display', serif"),
                                rx.text("Guadalajara, Jalisco, MX", color="#666", font_size="0.8rem",
                                       font_family="'Inter', sans-serif"),
                                spacing="0",
                            ),
                            spacing="4",
                            align_items="center",
                            width="100%",
                            padding="1.25rem",
                        ),
                        width="100%",
                        background="#111",
                        border="1px solid #1a1a1a",
                    ),
                    # Response time
                    rx.text(
                        "Tiempo de respuesta: 24-48 horas",
                        color="#444",
                        font_size="0.75rem",
                        letter_spacing="0.05em",
                        font_family="'Inter', sans-serif",
                        text_align="center",
                        padding_top="0.5rem",
                    ),
                    spacing="3",
                    width="100%",
                    class_name="fade-in-up delay-1",
                ),
                columns=rx.breakpoints(initial="1", lg="2"),
                spacing="6",
                width="100%",
                max_width="900px",
                margin="0 auto",
            ),
            padding_x=rx.breakpoints(initial="1rem", md="2rem"),
            padding_y="6rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        id="contact",
        background="#0a0a0a",
        border_top="1px solid #1a1a1a",
        width="100%",
    )


def footer():
    return rx.box(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.hstack(
                        rx.box(width="6px", height="6px", background="#8B0000", border_radius="50%"),
                        rx.text(
                            "NURSE TATTO",
                            color="white",
                            font_weight="900",
                            letter_spacing="0.2em",
                            font_family="'Playfair Display', serif",
                            font_size="0.9rem",
                        ),
                        spacing="2",
                        align_items="center",
                    ),
                    rx.spacer(),
                    rx.hstack(
                        rx.link(rx.icon(tag="camera", size=18, color="#444"), href="https://instagram.com/lahamy.ink",
                               is_external=True, _hover={"color": "#8B0000"}),
                        rx.link(rx.icon(tag="globe", size=18, color="#444"), href="https://facebook.com/lahamytattoo",
                               is_external=True, _hover={"color": "#8B0000"}),
                        rx.link(rx.icon(tag="message-circle", size=18, color="#444"), href="https://wa.me/52TUNUMERO",
                               is_external=True, _hover={"color": "#8B0000"}),
                        spacing="5",
                    ),
                    width="100%",
                    align_items="center",
                ),
                rx.box(height="1px", width="100%", background="#1a1a1a"),
                rx.text(
                    "© 2025 Nurse Tatto · Guadalajara, Jalisco",
                    color="#333",
                    font_size="0.75rem",
                    font_family="'Inter', sans-serif",
                    letter_spacing="0.05em",
                ),
                spacing="4",
                align_items="center",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
        ),
        padding_y="2rem",
        background="#080808",
        width="100%",
    )


# ─── Main Page ───────────────────────────────────────────────────────

def index():
    return rx.box(
        navbar(),
        hero_section(),
        portfolio_gallery(),
        styles_section(),
        about_section(),
        testimonials_section(),
        contact_section(),
        footer(),
        width="100%",
        min_height="100vh",
        background="#0a0a0a",
        style={"scroll_behavior": "smooth"},
    )


# ─── App Configuration ──────────────────────────────────────────────

app = rx.App(
    theme=themes.theme(
        appearance="dark",
        accent_color="red",
        gray_color="mauve",
        radius="none",
        scaling="100%",
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap",
        "animations.css",
    ],
    style={
        "scroll_behavior": "smooth",
        "scroll_padding_top": "80px",
        "*": {"box_sizing": "border-box"},
    },
    head_components=[
        rx.script(src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"),
        rx.script("""
            (function() {
                var checkEmailJS = setInterval(function() {
                    if (typeof emailjs !== 'undefined') {
                        emailjs.init('i-kJz81g1FcJ4KMBt');
                        console.log('EmailJS inicializado correctamente');
                        clearInterval(checkEmailJS);
                    }
                }, 100);
            })();
        """),
    ],
)

app.add_page(index, title="Nurse Tatto | LaHamy — Arte Oscuro en tu Piel")