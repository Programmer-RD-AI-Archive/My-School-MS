/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
import { Button } from "@material-ui/core";
import React from "react";
import "./Login.css";
import { auth, provider } from "./firebase";
import { useStateValue } from "./StateProvider";
import { actionTypes } from "./reducer";
function Login() {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  const [{}, dispatch] = useStateValue();
  const signIn = () => {
    auth
      .signInWithPopup(provider)
      .then((result) => {
        
        dispatch({
          type: actionTypes.SET_USER,
          user: result.user,
        });
      })
      .catch((error) => {
        alert(error.message);
      });
  };
  return (
    <div>
      <div className="login__container">
        <img
          src="https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/whatsapp-512.png"
          alt=""
        />
        <div className="login__text">
          <h1>
            {" "}
            <b> Sign In to Whatsapp Web Clone </b>{" "}
          </h1>
        </div>
        <Button onClick={signIn}>
          <h1>
            <b> Sign In With Google </b>
          </h1>
        </Button>
      </div>
    </div>
  );
}

export default Login;
