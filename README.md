# A ffdroid Flet app

An example of a minimal Flet app.

To run the app:

```bash
flet run src
```

## Internationalization

Create `.po` files with

```bash
./QuickTranslator.py -ll i -t -p ./src
```

Compile to `.mo` with

```
./QuickTranslator.py -ll i -c -p ./src
```

### TODO

- [ ] I18n is not working when switching language
