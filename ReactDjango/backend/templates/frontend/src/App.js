import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import Table from 'react-bootstrap/Table';

class App extends Component{
  componentDidMount() {
    // tag = "Django"
    var board= "Django"
    axios.get('http://localhost:8000/boards/?tag='+ "" + '&board=' + board, 
      
    )
      .then(res => {
        console.log(res.data);
        this.setState({
          boards: res.data
        });
      })
      .catch((error) => {
        console.log(error);
      })
  }
  render() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
  }
}

export default App;
