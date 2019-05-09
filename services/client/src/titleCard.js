import React from 'react';
import ReactDOM from 'react-dom';
import './titleCard.css';

const TitleCard = () => {
  return(
    <section className="titleCard">
        <br/>
        <h1 className="title">Jamie Christopher Webber</h1>
       
        <div className="subtitles">
          <h2 className="title">web developer</h2>
          <h2 className="title">composer/improviser</h2>
          <h2 className="title">creative audio programmer</h2>
        </div>
        <br/>
    </section>
  )
}

export default TitleCard;