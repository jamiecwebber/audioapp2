import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';


// new
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
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">Submit a sound</h1>
              <hr/><br/>
              <form action="/sounds" method="POST" encType="multipart/form-data">
          <div className="field">
            <input
              name="title" className="input"
              type="text" placeholder="Enter a title" required />
          </div>
          <div className="field">
            <input
              name="file" className="input"
              type="file" required />
          </div>
          <input
            type="submit" className="button is-primary is-fullwidth"
            value="Submit" />
        </form>
            </div>
          </div>
        </div>
      </section>
    )
  }
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);