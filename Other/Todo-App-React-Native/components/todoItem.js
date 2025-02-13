/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
import React, { useState } from "react";
import { StyleSheet, View, Text, TouchableOpacity } from "react-native";
import { MaterialIcons } from "@expo/vector-icons";
const TodoItem = ({ item, pressHandler }) => {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  return (
    <TouchableOpacity onPress={() => pressHandler(item.key)}>
      <View style={styles.item}>
        <MaterialIcons name="delete" size={24} color="#333" />
        <Text style={styles.itemText}>{item.text}</Text>
      </View>
    </TouchableOpacity>
  );
};
const styles = StyleSheet.create({
  item: {
    padding: 16,
    marginTop: 20,
    borderColor: "#bbb",
    borderWidth: 1,
    borderStyle: "dashed",
    borderRadius: 10,
    flex: 1,
    flexDirection: "row",
  },
  itemText: {
    marginLeft: 10,
  },
});
export default TodoItem;
