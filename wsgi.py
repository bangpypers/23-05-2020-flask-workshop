from workshop import create_app

app = create_app(config="config.dev")


if __name__ == "__main__":
    app.run()
