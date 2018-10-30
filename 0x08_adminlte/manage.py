from watermark.application import create_app

if __name__ == '__main__':
    app = create_app()
    
    print(app.url_map)
    
    app.run()
