# JavaScript

## 浏览器对象 BOM (Browser Object Model)

`window` 是最常见的浏览器对象，JavaScript中最常见的用法：

```javascript
window.onload = funtion(
  // TODO
);
```

就是给 `window` 对象的 `onload` 事件赋值回调函数，在 `onload` 事件被触发时调用函数来进行处理，通俗来讲就是页面加载完成后执行 TODO 的内容。

## HTML DOM (Document Object Model)

![ct_htmltree](ct_htmltree.gif)

为了便于对 HTML 进行操作，在 JavaScript 中将 HTML 文档抽象成了文档对象模型，即 DOM。通过 DOM 的接口，JavaScript 能够改变整个 HTML 显示的内容，比如：

```html
<--!index.html!-->
<html>
<body>

<p id="intro">Hello World!</p>

<script>
window.onload = function(
  var txt = document.getElementById("intro");
  txt.innerHTML = "你好，世界！";
);
</script>

</body>
</html>

```

## jQuery

JavaScript 的一个库，封装了对 DOM 和 BOM 的各种操作，提供了类似 CSS 中的选择器。优点是封装好，使用简单。缺点是慢慢慢慢。
