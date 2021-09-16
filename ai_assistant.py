class AI:
'''
This class will be used to make our assistant smarter.
'''

    __corpus = []
    __target_vector = []

    def prepare_corpus(self):
        """
        Подготовка модели для угадывания намерения пользователя
        """
        # corpus = []
        # target_vector = []
        for intent_name, intent_data in config["intents"].items():
            for example in intent_data["examples"]:
                self.__corpus.append(example)
                self.__target_vector.append(intent_name)

        training_vector = vectorizer.fit_transform(corpus)
        classifier_probability.fit(training_vector, target_vector)
        classifier.fit(training_vector, target_vector)

    def get_intent(self, request):
        """
        Получение наиболее вероятного намерения в зависимости от запроса пользователя
        :param request: запрос пользователя
        :return: наиболее вероятное намерение
        """
        best_intent = classifier.predict(vectorizer.transform([request]))[0]

        index_of_best_intent = list(classifier_probability.classes_).index(best_intent)
        probabilities = classifier_probability.predict_proba(vectorizer.transform([request]))[0]

        best_intent_probability = probabilities[index_of_best_intent]

        # при добавлении новых намерений стоит уменьшать этот показатель
        if best_intent_probability > 0.57:
            return best_intent