# 📝 TPC3

Neste TPC, o objetivo é criar um conversor de Markdown (MD) para HTML. O programa deverá ser capaz de processar e converter os seguintes elementos básicos de formatação presentes em uma Markdown Cheat Sheet:

## Author
<p><strong>Name:</strong> Fábio Magalhães</p>
<p><strong>Number:</strong> A104365</p>

## Results

O código é capaz de tranformar como esperado um ficheiro de entrada em formato Markdown para HTML.

Por exemplo, ficheiro de entrada `input.md`:
```markdown
# Heading 1
## Heading 2
### Heading 3

This is a **bold** text and this is an *italic* text.

This is a [link](https://example.com) and here is an image:

![Alt text](https://example.com/image.jpg)

1. First item
2. Second item
3. Third item
```

Retorna o seguinte HTML/ficheiro de saida `output.html`:
```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>

This is a <b>bold</b> text and this is an <i>italic</i> text.

This is a <a href="https://example.com">link</a> and here is an image:

<img src="https://example.com/image.jpg" alt="Alt text"/>

<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
</ol>
```

To run the program you can use:
```bash
python mdToHtml.py test.md output.html
```