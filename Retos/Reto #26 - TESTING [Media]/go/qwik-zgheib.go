package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

/* create file with name: <any_name>_test.go */

func TestHasFriday13th(t *testing.T) {
	detector := NewSimpleFriday13thDetector()

	tests := []struct {
		month       int
		year        int
		expected    bool
		expectedErr bool
	}{
		{10, 2023, false, false}, /* 13th October 2023 is not a Friday */
		{1, 2023, false, false},  /* 13th January 2023 is a Friday */
		{13, 2023, false, true},  /* Invalid month */
		{0, 2023, false, true},   /* Invalid month */
		{5, 2022, true, false},   /* 13th May 2022 is a Friday */
		{6, 2022, false, false},  /* 13th June 2022 is not a Friday */
		{11, 2023, true, false},  /* 13th November 2023 is a Friday */
		{-1, 2023, false, true},  /* Invalid month */
		{4, -1, false, true},     /* Invalid year */
		{8, 1999, true, false},   /* 13th August 1999 is a Friday */
	}

	for _, test := range tests {
		result, err := detector.HasFriday13th(test.month, test.year)
		if test.expectedErr {
			assert.Error(t, err)
		} else {
			assert.NoError(t, err)
		}
		assert.Equal(t, test.expected, result)
	}
}

