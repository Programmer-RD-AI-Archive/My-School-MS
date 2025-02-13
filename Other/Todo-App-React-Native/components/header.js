/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
import React, { useState } from "react";
import { StyleSheet, View, Text } from "react-native";
const Header = () => {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  return (
    <View style={styles.header}>
      <Text style={styles.title}>My Todos</Text>
    </View>
  );
};
const styles = StyleSheet.create({
  header: {
    height: 80,
    paddingTop: 38,
    backgroundColor: "coral",
  },
  title: {
    textAlign: "center",
    color: "gray",
    fontSize: 20,
    fontWeight: "bold",
  },
});
export default Header;
