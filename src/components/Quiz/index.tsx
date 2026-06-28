import {useState, useCallback} from 'react';
import type {ReactNode} from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

export type QuizQuestion = {
  question: string;
  options: string[];
  correctIndex: number;
  explanation?: string;
};

type QuizProps = {
  title?: string;
  questions: QuizQuestion[];
  storageKey?: string;
};

export default function Quiz({title = 'Quick Check', questions, storageKey}: QuizProps): ReactNode {
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [submitted, setSubmitted] = useState(false);

  const handleSelect = useCallback((qIndex: number, optionIndex: number) => {
    if (submitted) return;
    setAnswers((prev) => ({...prev, [qIndex]: optionIndex}));
  }, [submitted]);

  const handleSubmit = useCallback(() => {
    setSubmitted(true);
    if (storageKey && typeof window !== 'undefined') {
      const score = questions.reduce(
        (acc, q, i) => acc + (answers[i] === q.correctIndex ? 1 : 0),
        0,
      );
      const passed = score === questions.length;
      const stored = JSON.parse(localStorage.getItem('cv-quiz-results') || '{}');
      stored[storageKey] = {score, total: questions.length, passed, date: Date.now()};
      localStorage.setItem('cv-quiz-results', JSON.stringify(stored));
    }
  }, [answers, questions, storageKey]);

  const handleReset = useCallback(() => {
    setAnswers({});
    setSubmitted(false);
  }, []);

  const score = questions.reduce(
    (acc, q, i) => acc + (answers[i] === q.correctIndex ? 1 : 0),
    0,
  );
  const allAnswered = questions.every((_, i) => answers[i] !== undefined);

  return (
    <div className={styles.quiz}>
      <h3 className={styles.quizTitle}>{title}</h3>
      {questions.map((q, qIndex) => {
        const selected = answers[qIndex];
        const isCorrect = selected === q.correctIndex;
        return (
          <div key={qIndex} className={styles.question}>
            <p className={styles.questionText}>
              <strong>{qIndex + 1}.</strong> {q.question}
            </p>
            <div className={styles.options}>
              {q.options.map((option, oIndex) => {
                let optionClass = styles.option;
                if (submitted) {
                  if (oIndex === q.correctIndex) optionClass = clsx(optionClass, styles.correct);
                  else if (oIndex === selected) optionClass = clsx(optionClass, styles.incorrect);
                } else if (oIndex === selected) {
                  optionClass = clsx(optionClass, styles.selected);
                }
                return (
                  <button
                    key={oIndex}
                    type="button"
                    className={optionClass}
                    onClick={() => handleSelect(qIndex, oIndex)}
                    disabled={submitted}>
                    {option}
                  </button>
                );
              })}
            </div>
            {submitted && q.explanation && (
              <p className={clsx(styles.explanation, isCorrect ? styles.explanationOk : styles.explanationBad)}>
                {isCorrect ? '✅' : '❌'} {q.explanation}
              </p>
            )}
          </div>
        );
      })}
      <div className={styles.actions}>
        {!submitted ? (
          <button
            type="button"
            className="button button--primary"
            onClick={handleSubmit}
            disabled={!allAnswered}>
            Check Answers
          </button>
        ) : (
          <>
            <span className={styles.score}>
              Score: {score}/{questions.length}
              {score === questions.length ? ' 🎉' : ''}
            </span>
            <button type="button" className="button button--secondary" onClick={handleReset}>
              Try Again
            </button>
          </>
        )}
      </div>
    </div>
  );
}
