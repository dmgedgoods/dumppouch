package main

import (
    "github.com/rivo/tview"
    "github.com/gdamore/tcell/v2"
)

func main() {
    // Create a new primitive which is a full-screen application.
    app := tview.NewApplication()

    // Create a new text view and set some text to display.
    textView := tview.NewTextView().
        SetText("Hello, TUI world! Press 'q' to quit.")
        

    // Set up input capture to quit the application when 'q' is pressed.
    textView.SetInputCapture(func(event *tcell.EventKey) *tcell.EventKey {
        if event.Key() == tcell.KeyRune && event.Rune() == 'q' {
            app.Stop()
        }
        return event
    })

    // Set the root of the application to the text view and run the application.
    if err := app.SetRoot(textView, true).Run(); err != nil {
        panic(err)
    }
}

