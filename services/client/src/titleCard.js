import React from 'react';
// import ReactDOM from 'react-dom';
import './titleCard.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

const TitleCard = () => {
  return(
    <section className="titleCard">
        <h3>welcome to the personal site of</h3>
        <h1 className="title">Jamie Christopher Webber</h1>
       
        <div className="subtitles">
          <Link to='/dev/'><h2 className="title">web developer</h2></Link>
          <Link to='/music/'><h2 className="title">composer/improviser</h2></Link>
          <Link to='/audio/'><h2 className="title">creative audio programmer</h2></Link>
        </div>
        <br/>
    </section>
  )
}

export default TitleCard;