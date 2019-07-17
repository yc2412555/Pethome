<template>
  <div class="cyq">
    <div class="cyq-header">
      <router-view name="header"></router-view>
    </div>
    <div class="cyq-main">
      <router-view></router-view>
    </div>
    <div class="cyq-footer">
      <router-view name="footer"></router-view>
    </div>
  </div>
</template>

<script>
// import { Toast } from 'mint-ui'
export default {
  created () {
    // Toast('提示信息')
  }
}
</script>

<style lang="scss">
@font-face {
  font-family: 'iconfont';  /* project id 1267740 */
  src: url('//at.alicdn.com/t/font_1267740_kmrqrp7a86.eot');
  src: url('//at.alicdn.com/t/font_1267740_kmrqrp7a86.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1267740_kmrqrp7a86.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1267740_kmrqrp7a86.woff') format('woff'),
  url('//at.alicdn.com/t/font_1267740_kmrqrp7a86.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1267740_kmrqrp7a86.svg#iconfont') format('svg');
}
.icon {
  font-family: "iconfont";
}
html, body, div, span, h1, h2, h3,
h4, h5, h6, p, a, em, img, small, strike, strong,
b, u, i, dl, dt, dd, ol, ul, li, fieldset, form,
label, legend, table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, figure, figcaption, footer,
header, hgroup, main, menu, nav, section, summary, time, mark {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, footer, header, hgroup, main, menu, nav, section {
  display: block;
}
/* HTML5 hidden-attribute fix for newer browsers */
*[hidden] {
  display: none;
}
body {
  line-height: 1;
}
ol, ul {
  list-style: none;
}
blockquote, q {
  quotes: none;
}
blockquote:before, blockquote:after, q:before, q:after {
  content: "";
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
html, body {
  height: 100%;
}
.cyq {
  height: 100%;
  display: flex;
  flex-direction: column;

  &-main {
    flex: 1;
    overflow-x: hidden;
  }
}
</style>
