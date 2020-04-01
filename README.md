# Install

For install the package run:

```
$ pip install flask-vuejs
```

# Using

Import the Vue class in bootstrap flask file, see:

```ptyhon
from flask_vuejs import Vue
```

## Register extension
```ptyhon
Vue(app)
```

## With Factory
```ptyhon
vue = Vue()

def create_app():
    app = Flask(__name__)
    vue.init_app(app)
```

## Configuration

You can set the component directory, by default it uses 'static/components' folder, but, it can be easily changed.

```ptyhon
def create_app():
    app.config["FLASK_VUE_COMPONENT_DIRECTORY"] = "vuecomponent"
```
Remember, if you changed component directory, you'll should be rename this directory on 'static' folder application

## [JInja Template]

You can see how its works [here](https://github.com/pacotei/flask-vuejs/tree/master/sample_app)