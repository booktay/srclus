import React, { Component } from 'react';
import Button from '@material-ui/core/Button';

import './App.css';

import Header from "./components/Header";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header/>
        {/* <header className="App-header"> */}
          {/* <img src={logo} className="App-logo" alt="logo" /> */}
          {/* <Button variant="contained" color="primary">
            Hello World
          </Button> */}
        {/* </header> */}
      </div>
    );
  }
}

export default App;
