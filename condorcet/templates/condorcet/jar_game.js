import React, { Component } from 'react';
import "jar.css"; // Tell webpack that Button.js uses these styles


class Choice extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      choice: false
    }
  }

    render(){

    return(
      <button
        className="choice"
        style = {{background: this.props.type}}
        onClick={() => this.setState({clicked: true})}

      >
        <div style = {{color: 'white'}}>
          {this.props.type.toUpperCase()}   JAR
        </div>

      </button>

    );
        }
}


class Square extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false
    }
    this.handleClick = this.handleClick.bind(this);

  }

   handleClick() {
    this.setState({clicked:!this.state.button})

  }

  render() {

    var button = this.state.clicked;
    var btnStyle = {background: 'silver'}

     if(button){
       btnStyle = {background: this.props.value}
     }

    return (
        <button
        type = "button"
        style= {btnStyle}
        className="btn btn-info btn-circle"
        onClick={() => this.handleClick()}
      >

      </button>
    );
  }
}

class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      redjar: ['red','red', 'red', 'red', 'red','red', 'red','blue', 'blue', 'blue'],
      bluejar: ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red']
                 }
  }

  renderSquare(rand1) {


    if(rand1 == 1){

       var jar = this.state.bluejar

    }

    if(rand1 == 2){
       var jar = this.state.redjar
    }

    const rand2 = Math.floor(Math.random()*(jar.length-1));

    var color = jar[rand2]

    jar.splice(rand2, 1);

    if(rand1 == 1){

       this.state.bluejar = jar

    }

    if(rand1 == 2){
       this.state.redjar = jar
    }

    return(
     <Square value = {color} />);


  }

  renderChoice(color){
      return(
     <Choice type = {color} />);

    }





  render() {
    const rand1 = Math.floor(Math.random()*2)+1;


    return (
      <div className = 'board__box'>

        <div className = "neck">
        </div>
        <div className = "shine">
        </div>
        <div className = "shine2">
        </div>
        <div className = "lid">
        </div>
        <div className = "lid2">
        </div>
        <div className = "lid3">
        </div>

        <div className="grid-container">
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}
          {this.renderSquare(rand1)}

        </div>
        <div>
          {this.renderChoice('blue')}
          {this.renderChoice('red')}
        </div>

      </div>

    );
  }
}

class Game extends React.Component {
  render() {


    return (
      <div className="game">
        <div className="game-info">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);

const domContainer = document.querySelector('#marble_jar');
ReactDOM.render(e(Game), domContainer);
