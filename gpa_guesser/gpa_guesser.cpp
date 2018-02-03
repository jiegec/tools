#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

double grades[] = {0.0, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0};
const int grades_kind = sizeof(grades) / sizeof(grades[0]);

int main() {
  int known_score, num_unknown_courses, temp_score, sum_unknown_scores;
  vector<int> unknown_scores;
  vector<int> gpa_indexes;
  double known_weighted_grade_point, overall_GPA;
  char ogp[10], tmp[10];
  printf("已知课程的总学分：");
  scanf("%d", &known_score);
  printf("已知课程的总加权绩点：");
  scanf("%lf", &known_weighted_grade_point);
  printf("已知课程计算出的 GPA 应为：%.2lf\n",
         known_weighted_grade_point / known_score);
  printf("未知课程的个数：");
  scanf("%d", &num_unknown_courses);
  sum_unknown_scores = 0;
  for (int i = 0; i < num_unknown_courses; i++) {
    printf("未知课程 #%d 的学分：", i + 1);
    scanf("%d", &temp_score);
    sum_unknown_scores += temp_score;
    unknown_scores.push_back(temp_score);
    gpa_indexes.push_back(0);
  }
  printf("已知和未知课程的 GPA：");
  scanf("%lf", &overall_GPA);
  snprintf(ogp, sizeof(ogp), "%.2lf", overall_GPA);
  while (1) {
    double current_GPA = known_weighted_grade_point;
    for (int i = 0; i < num_unknown_courses; i++) {
      current_GPA += grades[gpa_indexes[i]] * unknown_scores[i];
    }
    current_GPA /= known_score + sum_unknown_scores;
    snprintf(tmp, sizeof(tmp), "%.2lf", current_GPA);
    if (strcmp(ogp, tmp) == 0) {
      printf("未知课程可能的 GPA 有：");
      for (int i = 0; i < num_unknown_courses; i++) {
        printf(" %.2lf", grades[gpa_indexes[i]]);
      }
      printf("\n");
    }
    gpa_indexes[num_unknown_courses - 1]++;
    int index = num_unknown_courses - 1;
    while (index >= 0 && gpa_indexes[index] == grades_kind) {
      gpa_indexes[index] = 0;
      index--;
      gpa_indexes[index]++;
    }
    if (index < 0)
      break;
  }
  return 0;
}