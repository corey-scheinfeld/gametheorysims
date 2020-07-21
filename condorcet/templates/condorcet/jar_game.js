
const e = React.createElement;

class Marble extends React.Component {

  render() {
    return (
      <button
        type = "button"
        style={{background: 'blue'}}
        className="btn btn-info btn-circle"
        onClick={() => this.props.onClick()}
      >
        {this.props.value}
      </button>
    );
  }
}

class Jar extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      circles: Array(10).fill(null), };
  }

  handleClick(i){
    const circles = this.state.circles.slice();
    circles[i] = 'red';
    this.setState({circles: circles});
  }

  renderMarble(i){
    return(
      <Marble
      value={this.state.circles[i]}
      onClick = {()=> this.handleClick(i)}
      />
  );
  }

  render() {
    return (
      <div>
        <div className="board-row">
          {this.renderMarble(0)}
          {this.renderMarble(1)}
          {this.renderMarble(2)}
          {this.renderMarble(3)}
        </div>
        <div className="board-row">

          {this.renderMarble(4)}
          {this.renderSquare(5)}
          {this.renderMarble(6)}
        </div>
        <div className="board-row">
          {this.renderMarble(7)}
          {this.renderMarble(8)}
        </div>
        <div className="board-row">
          {this.renderMarble(9)}
      </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }

  ReactDOM.render(
    <Game />,
    document.getElementById('root')
  );
