import React from 'react';
import ReactDOM from 'react-dom';

const Form = () => {
  return(
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
  )
}

export default Form;