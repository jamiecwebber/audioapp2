import React, { Component } from 'react';
// import ReactDOM from 'react-dom';
import axios from 'axios';

class Form extends Component {

  addSound(event) {
    event.preventDefault();
    console.log(event);
    const data = new FormData();
    data.append('title', this.state.title);
    data.append('file', this.uploadInput.files[0]);
    console.log(process.env.REACT_APP_USERS_SERVICE_URL)
    axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/sounds`, data)
    .then((res) => { 
      console.log(res);
    })
    .catch((err) => { console.log(err); });
  }

  render () {
    return(
      <form action={this.addSound} encType="multipart/form-data">
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
    )
  }
}

export default Form;