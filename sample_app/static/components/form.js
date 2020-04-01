Vue.component("task-form", {
  template: `<form id="form-vue"><input type="text" name="task"/></form>`
});

new Vue({
  el: "#app",
  data: {
    title: "Task Form"
  }
});
