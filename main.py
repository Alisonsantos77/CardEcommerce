import flet as ft


def main(page: ft.Page):
    page.title = "Card ECommerce"
    page.bgcolor = ft.colors.BLACK
    page.scroll = ft.ScrollMode.AUTO
    page.window_height = 1024
    page.window_resizable = False
    page.window_maximizable = False

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5
        main_image.update()
        options.update()

    product_images = ft.Container(
        col={'xs': 12, 'sm': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9 / 16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                main_image := ft.Image(
                    src='assets/robo3.png',
                    width=400,
                    height=400,
                    fit=ft.ImageFit.CONTAIN,
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='assets/robo2.png',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='assets/robo1.png',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='assets/robo4.png',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='assets/robo3.png',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),
                    ]
                )
            ]
        )
    )
    product_details = ft.Container(
        col={'xs': 12, 'sm': 6},
        padding=ft.padding.all(20),
        bgcolor=ft.colors.BLACK,
        aspect_ratio=9 / 16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='Robo',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Robo Inteligente',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Doméstico',
                    color=ft.colors.GREY,
                    italic=True,
                ),
                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 399,99',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=30,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            spacing=10,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        ),
                        ft.Tabs(
                            selected_index=0,
                            height=150,
                            indicator_color=ft.colors.AMBER,
                            label_color=ft.colors.AMBER,
                            unselected_label_color=ft.colors.GREY,
                            tabs=[
                                ft.Tab(
                                    text='Descrição',
                                    content=ft.Container(
                                        padding=ft.padding.all(10),
                                        content=ft.Text(
                                            value='Conheça nosso mini robô amigo: compacto, inteligente e repleto de '
                                                  'personalidade! Com habilidades interativas avançadas, '
                                                  'ele pode ajudar em tarefas diárias e manter você entretido com '
                                                  'jogos. Com design moderno e funcionalidades inovadoras, '
                                                  'é o companheiro perfeito para sua casa. Garanta o seu e descubra '
                                                  'uma nova forma de interagir com a tecnologia!',
                                            color=ft.colors.GREY,
                                        )
                                    )
                                ),
                                ft.Tab(
                                    text='Como Funciona',
                                    content=ft.Container(
                                        padding=ft.padding.all(10),
                                        content=ft.Text(
                                            value='O mini robô amigo é ativado com um simples toque e responde aos '
                                                  'seus comandos e movimentos através de sensores inteligentes. Com '
                                                  'uma interface de voz amigável, ele pode ajudar em tarefas diárias, '
                                                  'contar piadas e jogar jogos interativos, proporcionando uma '
                                                  'experiência tecnológica envolvente e divertida.',
                                            color=ft.colors.GREY,
                                        )
                                    )
                                ),
                                ft.Tab(
                                    text='Como Usar',
                                    content=ft.Container(
                                        padding=ft.padding.all(10),
                                        content=ft.Text(
                                            value='Para usar o mini robô amigo, basta ligá-lo e interagir! Ele '
                                                  'responde aos seus comandos e movimentos através de sensores '
                                                  'inteligentes. Utilize sua interface de voz para pedir ajuda em '
                                                  'tarefas, jogar jogos ou simplesmente conversar. É fácil e '
                                                  'intuitivo, tornando a tecnologia acessível a todos!',
                                            color=ft.colors.GREY,
                                        )
                                    )
                                ),
                            ],

                        ),
                        ft.ResponsiveRow(
                            columns=12,
                            controls=[
                                ft.Dropdown(
                                    col=6,
                                    label='Cor',
                                    label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                                    border_width=0.5,
                                    border_color=ft.colors.GREY,
                                    options=[
                                        ft.dropdown.Option(text='Branco'),
                                        ft.dropdown.Option(text='Verde'),
                                        ft.dropdown.Option(text='Azul'),
                                    ]
                                ),
                                ft.Dropdown(
                                    col=6,
                                    label='Quantidade',
                                    label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                                    border_width=0.5,
                                    border_color=ft.colors.GREY,
                                    options=[
                                        ft.dropdown.Option(text=f'{num} unid.') for num in range(1, 11)
                                    ]
                                ),

                            ]
                        ),
                        ft.Container(expand=True),

                        ft.ElevatedButton(
                            width=900,
                            text='Adicionar a lista de desejos',
                            style=ft.ButtonStyle(
                                padding=ft.padding.all(20),
                                side={
                                    ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                                },
                                bgcolor={
                                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                                },
                                color={
                                    ft.MaterialState.DEFAULT: ft.colors.WHITE,
                                    ft.MaterialState.HOVERED: ft.colors.BLACK,

                                }
                            )
                        ),
                        ft.ElevatedButton(
                            width=900,
                            text='Adicionar ao carrinho',
                            style=ft.ButtonStyle(
                                padding=ft.padding.all(20),
                                side={
                                    ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                                },
                                bgcolor={
                                    ft.MaterialState.DEFAULT: ft.colors.AMBER,
                                },
                                color={
                                    ft.MaterialState.DEFAULT: ft.colors.BLACK,

                                }
                            )
                        ),
                    ]
                )
            ]
        ),
    )

    layout = ft.Container(
        alignment=ft.alignment.center,
        height=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details,
            ]
        )
    )

    page.add(layout)


ft.app(target=main, assets_dir='assets')
