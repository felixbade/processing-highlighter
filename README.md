# processing-highlighter
A JS syntax highlighter for the Processing language.

## Features
- Uses the same [word lists](https://github.com/processing/processing/blob/master/java/keywords.txt) as the official Processing IDE
- Uses the same colors as the official Processing IDE

## Bugs
- Some character combinations get lost (this is bad: the highlighted code can be different than the original)
- Block quotes don't work
- Quoted strings don't work

## Usage

Import the highlighter and the colors

```html
<script src="processing-syntax-hilighter.js"></script>
<link rel="stylesheet" href="processing-syntax-hilighting.css" type="text/css" />
```

Mark the elements that you want to be highlighted with `processing-code` class.

```html
<pre class="processing-code">void setup() {
  fullScreen();
}</pre>
```
