---
name: Contrast Issue
about: Describe the issue with the contrasts
title: ''
labels: ''
assignees: ''

---

# Brief Summary of Issue

The primary issue is...

## OpenNeuro Study

`ID`: ds000000
`contrast file`:  ds000000-taskname_contrasts.json

## Recommended Change

The recommendation is to use the following contrast list:

```python
{
    "Contrasts": [
        {
          "Name": "feedback",
          "ConditionList": [
            "trial_type.feedback"
          ],
          "Weights": [
            1
          ],
          "Test": "t"
        }
      ]
}
```

## Improvements via this contrast

This contrast is a better estimate of the [...] process.
