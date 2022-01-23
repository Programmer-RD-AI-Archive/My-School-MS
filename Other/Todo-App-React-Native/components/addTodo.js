/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
import React, { useState } from "react";
import {
  StyleSheet,
  View,
  TextInput,
  TouchableOpacity,
  Button,
} from "react-native";
const AddTodo = ({ submitHandler }) => {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  const [text, setText] = useState(null);
  const ChangeHandler = (value) => {
    setText(value);
  };
  return (
    <View>
      <TextInput
        style={styles.input}
        placeholder="New Todo..."
        onChangeText={ChangeHandler}
        clearButtonMode="always"
        value={text}
      />
      <Button
        onPress={() => {
          submitHandler(text);
          setText("");
        }}
        title="Add Todo"
        color="coral"
      />
    </View>
  );
};
const styles = StyleSheet.create({
  input: {
    marginBottom: 10,
    paddingHorizontal: 8,
    paddingVertical: 6,
    borderBottomWidth: 1,
    borderBottomColor: "#ddd",
  },
});
export default AddTodo;
