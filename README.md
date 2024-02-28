# Kafka Mini Project

## Overview

This project is about learning Apache Kafka's core concepts and applying them through practical scenarios. Here's what I've learned and implemented.

## Learning Outcomes

- **Kafka Architecture**: Understood the basic structure and components.
- **Zookeeper**: Learned its role in Kafka for managing cluster coordination.
- **Producers and Consumers**: Gained insight into how data is produced and consumed in Kafka.
- **Topics and Partitions**: Explored how Kafka uses topics and partitions for data distribution.
- **Consumer Groups**: Learned how consumer groups are used for efficient data consumption.

## Implementation

Implemented two scenarios to understand Kafka's workings:

1. **Single Broker, 1 Partition**: Basics of message production and consumption.
2. **Single Broker, 2 Partitions**: How partitions affect data distribution and consumption.

### Setup

- **Required Packages**: `kafka-python` for Kafka interaction, `Faker` for generating fake data.
- **Installation**: Run `pip install kafka-python Faker`.

### Running the Scenarios

1. Make sure Kafka and Zookeeper services are running.
2. Run the Python script `python producer.py` to publish messages to the Topic
4. Run the Python script `python consumer.py` to consume messages from the Topic

## Conclusion

This project helped me understand Kafka's fundamental concepts and how to implement them in Python. It's a step towards mastering Kafka for data streaming and processing applications.
