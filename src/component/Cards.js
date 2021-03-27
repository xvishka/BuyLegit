import React from 'react'
import {Card} from 'react-bootstrap';
import CardDeck from "react-bootstrap/CardDeck";
// import ApicemData from './assets/ApicemData.json';
//import * as data from './assets/ApicemData.json';
import data from './assets/ApicemData.json';


function Cards() {
    const cardInfo = [
        {image: "https://i.ebayimg.com/images/g/Y98AAOSwGAhftuuC/s-l1600.jpg", title: "", text: "Cover for Apple iPhone 12 11 Pro 7 8 Plus X XR XS MAX SE 12 Mini Shockproof Clear Case "},
        {image: "https://i.ebayimg.com/images/g/CcEAAOSwxFRgNKOD/s-l1600.jpg", title: "", text: "Apple iPhone 12 Pro Max 11 12 Mini Shockproof Clear Crystal Case Phone Cover"},
        {image: "https://i.ebayimg.com/images/g/iaUAAOSwlXJf8oKt/s-l1600.jpg", title: "", text: "SHOCKPROOF plating clear Case For iPhone 12 11 Pro MAX Mini XR XS 7/8 PLUS Cover"},
        {image: "https://i.ebayimg.com/images/g/FC0AAOSwm~lfa4lT/s-l1600.jpg", title: "", text: "For iphone 11 Case Cover w/Screen & Clip Holster fit Otterbox Defender"},
        {image: "https://i.ebayimg.com/images/g/v9MAAOSwBthf4Uzv/s-l1600.jpg", title: "", text: "For iPhone 11/12 Pro Max Shockproof Defender Case With Stand Belt Clip Holster "},
        {image: "https://i.ebayimg.com/images/g/Kc0AAOSw-39f9oPa/s-l1600.jpg", title: "", text: "For iPhone 12 11 Pro Max XS XR X 8 7 Plating Shockproof Matte Clear Case Cover "},
        {image: "https://i.ebayimg.com/images/g/dKEAAOSwbj9elrXi/s-l1600.jpg", title: "", text: "For iPhone 11 Pro Max ,12 Pro ,11 Case Hybrid Heavy Duty Clear Belt Clip Cover"},
        {image: "https://i.ebayimg.com/images/g/Bc0AAOSw1xZcdlNp/s-l1600.jpg", title: "", text: "For Apple iPhone 11/Pro/Max/XS Max/XR/X Clear Belt Clip Cover "}
    ]
    const renderCards = (card, index) =>{
        return(
            <Card style={{ width: '18rem' }} key={index} className="box">   
            <Card.Img variant="top" className="cardImage" src={card.image} />
            <Card.Body>
                <Card.Title>{card.title}</Card.Title>
                <Card.Text className="text">
                {card.text}
                </Card.Text>
            </Card.Body>
            </Card>
        )
    }
    return (
        <div className="grid">
            {cardInfo.map(renderCards)}
        </div>
    )
}

export default Cards
