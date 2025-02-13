/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
import React from "react";
const Head = (props) => {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  return (
    <div>
      <h5>
        <b>Copyright © 2020 RanugaD</b>
      </h5>
      <img
        width="125"
        src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Messenger_colored_svg-512.png"
        alt="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Messenger_colored_svg-512.png"
      />
      <h1>
        <b>Messenger Clone</b>
      </h1>
      <h3>Welcome {props.username}</h3>
    </div>
  );
};
export default Head;
