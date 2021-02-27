  function Square(props) {
    var button = props.clicked;
    var btnStyle = {background: 'silver'}
    if(button){
      btnStyle = {background: props.value}
          }
          return (
            <button className="btn btn-info btn-circle" onClick={props.onClick} style= {btnStyle}
            disabled = {props.disabled}
            >
            </button>
          );
        }

    class Board extends React.Component {
      constructor(props) {
        super(props);
        this.state = {
          redjar: ['red','red', 'red', 'red', 'red','red', 'red','blue', 'blue', 'blue'],
          bluejar: ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red'],
          btnStyle: false,
          btnColors: Array(10).fill('silver'),
          signal: 'silver'
                     }

      }

      renderSquare(i, color) {
        return (
         <Square disabled = {this.state.btnStyle} clicked = {this.state.btnStyle} value = {this.state.btnColors[i]} onClick={() => this.handleClick(i, color)}/>);


      }

      handleClick(i, color){
        this.setState({btnStyle: true});
        const rainbow = this.state.btnColors.slice();
        rainbow[i] = color;
        this.setState({btnColors: rainbow});
        this.setState({signal: color});
        document.getElementById('signal').value = color;
}


      render() {
        const colors = this.props.marbles



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
              {this.renderSquare(0, colors[0])}
              {this.renderSquare(1, colors[1])}
              {this.renderSquare(2, colors[2])}
              {this.renderSquare(3, colors[3])}
              {this.renderSquare(4, colors[4])}
              {this.renderSquare(5, colors[5])}
              {this.renderSquare(6, colors[6])}
              {this.renderSquare(7, colors[7])}
              {this.renderSquare(8, colors[8])}
              {this.renderSquare(9, colors[9])}

            </div>
            <div className='game'>
            <input type = "hidden" name = "signal" id = "signal" value = {this.state.signal}/>

            </div>

          </div>

        );
      }
    }

    class Game extends React.Component {
      constructor(props) {
        super(props);
        this.state = {
          redjar: ['red','red', 'red', 'red', 'red','red', 'red','blue', 'blue', 'blue'],
          bluejar: ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red']

        }
      }

      render() {
        const rand1 = this.props.jar

        var jar = [];

        if(rand1 == 'True'){

            jar = this.state.bluejar

        }

        if(rand1 == 'False'){
            jar = this.state.redjar
        }


        var colors = [];
        var i = 0;

        while(i < 10){
           const rand2 = Math.floor(Math.random()*(jar.length-1));

        var color = jar[rand2]
        colors[i] = color

        jar.splice(rand2, 1);

        if(rand1 == 'True'){

           this.state.bluejar = jar

        }

        if(rand1 == 'False'){
           this.state.redjar = jar
        }
          i = i+1;
        }


        return (
          <div className="game">

            <div className="game-info">
              <Board marbles = {colors} />
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

    const domContainer = document.querySelector('#root');
    ReactDOM.render(<Game jar = {domContainer.dataset.jar} />, domContainer);
