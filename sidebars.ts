import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Python Course',
      collapsed: false,
      items: [
        'python/course-overview',
        {
          type: 'category',
          label: 'Module 1: Fundamentals',
          items: [
            'python/fundamentals/introduction',
            'python/fundamentals/setup',
            'python/fundamentals/variables-types',
            'python/fundamentals/operators',
            'python/fundamentals/input-output',
          ],
        },
        {
          type: 'category',
          label: 'Module 2: Control Flow',
          items: [
            'python/control-flow/conditionals',
            'python/control-flow/for-loops',
            'python/control-flow/while-loops',
          ],
        },
        {
          type: 'category',
          label: 'Module 3: Data Structures',
          items: [
            'python/data-structures/lists',
            'python/data-structures/tuples-sets',
            'python/data-structures/dictionaries',
            'python/data-structures/strings',
          ],
        },
        {
          type: 'category',
          label: 'Module 4: Functions',
          items: [
            'python/functions/functions-basics',
            'python/functions/scope-closures',
            'python/functions/functional-programming',
          ],
        },
        {
          type: 'category',
          label: 'Module 5: OOP',
          items: [
            'python/oop/classes-objects',
            'python/oop/inheritance',
            'python/oop/polymorphism',
          ],
        },
        {
          type: 'category',
          label: 'Module 6: Files & Errors',
          items: [
            'python/files-errors/exception-handling',
            'python/files-errors/file-io',
            'python/files-errors/json-csv',
          ],
        },
        {
          type: 'category',
          label: 'Module 7: Intermediate',
          items: [
            'python/intermediate/comprehensions',
            'python/intermediate/generators',
            'python/intermediate/decorators',
            'python/intermediate/context-managers',
          ],
        },
        {
          type: 'category',
          label: 'Module 8: Advanced',
          items: [
            'python/advanced/modules-packages',
            'python/advanced/testing',
            'python/advanced/type-hints',
            'python/advanced/async',
            'python/advanced/best-practices',
          ],
        },
        {
          type: 'category',
          label: 'Quizzes',
          items: [
            'python/quizzes/module-1',
            'python/quizzes/module-2',
            'python/quizzes/module-3',
            'python/quizzes/module-4',
            'python/quizzes/module-5',
            'python/quizzes/module-6',
            'python/quizzes/module-7',
            'python/quizzes/module-8',
            'python/quizzes/dsa',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'DSA Patterns',
      items: [
        {
          type: 'category',
          label: 'Sliding Window',
          items: ['max-sum-subarray', 'longest-substring'],
        },
        {
          type: 'category',
          label: 'HashMap',
          items: ['two-sum', 'contains-duplicate', 'group-anagrams'],
        },
        {
          type: 'category',
          label: 'Stack',
          items: ['valid-parentheses', 'daily-temperatures'],
        },
        {
          type: 'category',
          label: 'Binary Search',
          items: ['binary-search', 'search-insert-position'],
        },
        {
          type: 'category',
          label: 'Two Pointers',
          items: ['valid-palindrome', 'container-water'],
        },
        {
          type: 'category',
          label: 'Dynamic Programming',
          items: ['climbing-stairs', 'house-robber'],
        },
        {
          type: 'category',
          label: 'BFS / DFS',
          items: ['max-depth-tree', 'number-of-islands'],
        },
        {
          type: 'category',
          label: 'Heap',
          items: ['kth-largest'],
        },
        {
          type: 'category',
          label: 'Linked List',
          items: ['reverse-linked-list'],
        },
      ],
    },
  ],
};

export default sidebars;
