import Vue from "vue";
import HelloWorld from "./components/HelloWorld";
import store from "./store";

new Vue({
  store,
  components: {
    HelloWorld,
  },
}).$mount("#app");
