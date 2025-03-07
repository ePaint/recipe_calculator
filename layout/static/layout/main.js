var valid_events = ['click', 'submit'];
document.addEventListener('htmx:afterRequest', function (event) {
    const triggering_event = event.detail?.requestConfig?.triggeringEvent?.type;
    if (triggering_event && !valid_events.includes(triggering_event)) return;
    // window.scrollTo(0, 0);
});