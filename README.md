# pygame-web-template
Pygame-web(pygbag) template for personal use.

## Usage
If you use this locally, try:

```sh
pip install -r requirements.txt
pygbag example
```

If use `Github codespace`, try:
```sh
pygbag --build example
python -m http.server -d example/build/web
```
(`pygbag` dev server replaces all CDN addresses to `localhost`, so we use `http.server` instead.)

You can find other usage in [pygbag repo](https://github.com/pygame-web/pygbag).