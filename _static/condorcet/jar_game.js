

function _getRequireWildcardCache() { if (typeof WeakMap !== "function") return null; var cache = new WeakMap(); _getRequireWildcardCache = function _getRequireWildcardCache() { return cache; }; return cache; }

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } if (obj === null || _typeof(obj) !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

function _instanceof(left, right) { if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) { return !!right[Symbol.hasInstance](left); } else { return left instanceof right; } }

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

function _classCallCheck(instance, Constructor) { if (!_instanceof(instance, Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } return _assertThisInitialized(self); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Date.prototype.toString.call(Reflect.construct(Date, [], function () {})); return true; } catch (e) { return false; } }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }

//
var Choice = /*#__PURE__*/function (_React$Component) {
  _inherits(Choice, _React$Component);

  var _super = _createSuper(Choice);

  function Choice(props) {
    var _this;

    _classCallCheck(this, Choice);

    _this = _super.call(this, props);
    _this.state = {
      choice: false
    };
    return _this;
  }

  _createClass(Choice, [{
    key: "render",
    value: function render() {
      var _this2 = this;

      return /*#__PURE__*/_react.default.createElement("button", {
        className: "choice",
        style: {
          background: this.props.type
        },
        onClick: function onClick() {
          return _this2.setState({
            clicked: true
          });
        }
      }, /*#__PURE__*/_react.default.createElement("div", {
        style: {
          color: 'white'
        }
      }, this.props.type.toUpperCase(), "   JAR"));
    }
  }]);

  return Choice;
}(_react.default.Component);

var Square = /*#__PURE__*/function (_React$Component2) {
  _inherits(Square, _React$Component2);

  var _super2 = _createSuper(Square);

  function Square(props) {
    var _this3;

    _classCallCheck(this, Square);

    _this3 = _super2.call(this, props);
    _this3.state = {
      clicked: false
    };
    _this3.handleClick = _this3.handleClick.bind(_assertThisInitialized(_this3));
    return _this3;
  }

  _createClass(Square, [{
    key: "handleClick",
    value: function handleClick() {
      this.setState({
        clicked: !this.state.button
      });
    }
  }, {
    key: "render",
    value: function render() {
      var _this4 = this;

      var button = this.state.clicked;
      var btnStyle = {
        background: 'silver'
      };

      if (button) {
        btnStyle = {
          background: this.props.value
        };
      }

      return /*#__PURE__*/_react.default.createElement("button", {
        type: "button",
        style: btnStyle,
        className: "btn btn-info btn-circle",
        onClick: function onClick() {
          return _this4.handleClick();
        }
      });
    }
  }]);

  return Square;
}(_react.default.Component);

var Board = /*#__PURE__*/function (_React$Component3) {
  _inherits(Board, _React$Component3);

  var _super3 = _createSuper(Board);

  function Board(props) {
    var _this5;

    _classCallCheck(this, Board);

    _this5 = _super3.call(this, props);
    _this5.state = {
      redjar: ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue'],
      bluejar: ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red']
    };
    return _this5;
  }

  _createClass(Board, [{
    key: "renderSquare",
    value: function renderSquare(rand1) {
      if (rand1 == 1) {
        var jar = this.state.bluejar;
      }

      if (rand1 == 2) {
        var jar = this.state.redjar;
      }

      var rand2 = Math.floor(Math.random() * (jar.length - 1));
      var color = jar[rand2];
      jar.splice(rand2, 1);

      if (rand1 == 1) {
        this.state.bluejar = jar;
      }

      if (rand1 == 2) {
        this.state.redjar = jar;
      }

      return /*#__PURE__*/_react.default.createElement(Square, {
        value: color
      });
    }
  }, {
    key: "renderChoice",
    value: function renderChoice(color) {
      return /*#__PURE__*/_react.default.createElement(Choice, {
        type: color
      });
    }
  }, {
    key: "render",
    value: function render() {
      var rand1 = Math.floor(Math.random() * 2) + 1;
      return /*#__PURE__*/_react.default.createElement("div", {
        className: "board__box"
      }, /*#__PURE__*/_react.default.createElement("div", {
        className: "neck"
      }), /*#__PURE__*/_react.default.createElement("div", {
        className: "shine"
      }), /*#__PURE__*/_react.default.createElement("div", {
        className: "shine2"
      }), /*#__PURE__*/_react.default.createElement("div", {
        className: "lid"
      }), /*#__PURE__*/_react.default.createElement("div", {
        className: "lid2"
      }), /*#__PURE__*/_react.default.createElement("div", {
        className: "lid3"
      }), /*#__PURE__*/_react.default.createElement("div", {
        className: "grid-container"
      }, this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1), this.renderSquare(rand1)), /*#__PURE__*/_react.default.createElement("div", null, this.renderChoice('blue'), this.renderChoice('red')));
    }
  }]);

  return Board;
}(_react.default.Component);

var Game = /*#__PURE__*/function (_React$Component4) {
  _inherits(Game, _React$Component4);

  var _super4 = _createSuper(Game);

  function Game() {
    _classCallCheck(this, Game);

    return _super4.apply(this, arguments);
  }

  _createClass(Game, [{
    key: "render",
    value: function render() {
      return /*#__PURE__*/_react.default.createElement("div", {
        className: "game"
      }, /*#__PURE__*/_react.default.createElement("div", {
        className: "game-info"
      }, /*#__PURE__*/_react.default.createElement(Board, null)), /*#__PURE__*/_react.default.createElement("div", {
        className: "game-info"
      }, /*#__PURE__*/_react.default.createElement("div", null), /*#__PURE__*/_react.default.createElement("ol", null)));
    }
  }]);

  return Game;
}(_react.default.Component); // ========================================


var domContainer = document.querySelector('marble_jar');
ReactDOM.render(e(Game), domContainer);
