# pui-css-dropdowns

A CSS dropdowns component that can be installed via this npm package.
This package provides all of the CSS you need to use the component.



## Installation

To install the package from the command line:

```
npm install pui-css-dropdowns
```

## Usage

Note that this requires the Bootstrap JavaScript.

```html
<div class="dropdown btn-group">
  <button id="dropdown-button-1" class="dropdown-toggle btn btn-default" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Button Dropdown
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu" role="menu" aria-labelledby="dropdown-button-1">
    <li role="presentation">
      <a href="http://www.google.com" role="menuitem">Google</a>
    </li>
    <li class="divider mvn"></li>
    <li role="presentation">
      <a href="http://www.yahoo.com" role="menuitem">Yahoo</a>
    </li>
    <li class="divider mvn"></li>
    <li role="presentation">
      <a href="http://www.aol.com" role="menuitem">Aol</a>
    </li>
  </ul>
</div>
```


You can find more examples of the dropdowns component in the [pui style guide](http://styleguide.pivotal.io/)


*****************************************

This is a component of Pivotal UI, a collection of [React](https://facebook.github.io/react/) and CSS components for rapidly building and prototyping UIs.

[Styleguide](http://styleguide.pivotal.io)
[Github](https://github.com/pivotal-cf/pivotal-ui)
[npm](https://www.npmjs.com/browse/keyword/pivotal%20ui%20modularized)

(c) Copyright 2016 Pivotal Software, Inc. All Rights Reserved.
