/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
import React from "react";
import "./HomePageBanner.css";
function HomePageBanner() {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  return (
    <div className="banner">
      <img
        src="https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/whatsapp-512.png"
        alt=""
      />
      <div className="login__text">
        <h1>
          <b>
            <i> Whatsapp web clone </i>
          </b>
        </h1>
      </div>
    </div>
  );
}

export default HomePageBanner;
