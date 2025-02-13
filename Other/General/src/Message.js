/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
import React, { forwardRef } from "react";
import { Card, CardContent, Typography } from "@material-ui/core";
import "./Message.css";

const Message = forwardRef(({ username, message }, ref) => {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  const isUser = username === message.username;
  return (
    <div ref={ref} className={`message ${isUser && "message__user"} `}>
      <Card className={isUser ? "message__userCard" : "message__guestCard"}>
        <CardContent>
          <Typography color="white" variant="h5" component="h2">
            {!isUser && `${message.username} : `}
            {message.message}
          </Typography>
        </CardContent>
      </Card>
    </div>
  );
});

export default Message;
