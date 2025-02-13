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
  FlatList,
  Text,
  Alert,
  Keyboard,
  TouchableWithoutFeedback,
} from "react-native";
const SandBox = () => {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  return (
    <View style={styles.container}>
      <Text style={styles.boxOne}>One</Text>
      <Text style={styles.boxTwo}>Two</Text>
      <Text style={styles.boxThree}>Three</Text>
      <Text style={styles.boxFour}>Four</Text>
    </View>
  );
};
const styles = StyleSheet.create({
  container: {
    // flex: 1,
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    paddingTop: 40,
    backgroundColor: "#ddd",
  },
  boxOne: {
    flex: 1,
    backgroundColor: "violet",
    padding: 10,
  },
  boxTwo: {
    flex: 2,
    backgroundColor: "gold",
    padding: 20,
  },
  boxThree: {
    flex: 3,
    backgroundColor: "coral",
    padding: 30,
  },
  boxFour: {
    flex: 4,
    backgroundColor: "blue",
    padding: 40,
  },
});
export default SandBox;
