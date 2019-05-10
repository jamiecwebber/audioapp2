import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import Form from './form';
import TitleCard from './titleCard'
import Header from './header'
import './index.css'


class App extends Component {
  constructor() {
    super();
    this.getUsers();
  }
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/sounds`)
    .then((res) => { console.log(res); })
    .catch((err) => { console.log(err); });
  }
  render() {
    return (
      <div className="fullPage">
        
        <div className="bodyContainer">
          <Header />
          <TitleCard />
        </div>
        <Form />
      </div>
    )
  }
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);