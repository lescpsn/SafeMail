ReactDOM.render(
  React.createElement("h1", null, "Hello, world!"),
  document.getElementById('example'),
  function () {
    console.log('渲染结束回调函数在这里!')
  }
);