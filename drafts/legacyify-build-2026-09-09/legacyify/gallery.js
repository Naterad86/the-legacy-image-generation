/* Local-only gallery. No network calls, image uploads, or generation. */
(() => {
  'use strict';
  const data = window.LEGACY_GALLERY || window.galleryData || window.GALLERY_DATA || {};
  const $ = (id) => document.getElementById(id);
  const text = (id, value) => { $(id).textContent = value || ''; };
  const node = (tag, className, value) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (value !== undefined) element.textContent = String(value);
    return element;
  };
  const path = (value) => {
    const raw = typeof value === 'object' && value ? value.src || value.path || value.url : value;
    if (typeof raw !== 'string' || /^(?:javascript|vbscript|data):/i.test(raw.trim())) return '';
    return raw.replace(/\\/g, '/');
  };
  const list = (value) => Array.isArray(value) ? value : value ? [value] : [];
  const actions = list(data.actions);
  let activeIndex = 0;
  let exampleIndex = 0;
  let view = 'output';
  let feedbackTimer;

  const defaultCommands = {
    character: 'Legacyify Character. Use the attached image as the task input and the approved character master as the sole identity authority. Inspect the source, state the supported boundary, then make one generation request for one result. Preserve the defining face, mane or hair, proportions, tail, and illustrated character style. Apply only the requested controlled change.',
    scene: 'Legacyify Scene. Inspect the attached image, preserve its focal meaning, framing, major spatial relationships, and consequential details. Select and state a suitable Legacy rendering profile, then make one generation request for one result. Keep any exact branding bound to its approved master. Record the result and any limitations.',
    together: 'Legacyify Together. Use the attached scene for composition and scene content, and the approved character master for identity. Create one coherent character-in-scene result with shared perspective, contact, light, and shadows. Keep the character illustrated and use the declared environment profile. Inspect the supported boundary first, then make one generation request for one result.'
  };

  function asset(example, type) {
    const supplied = type === 'source' ? example.source || example.before : example.output || example.after;
    return path(supplied);
  }

  function examples(action) {
    if (list(action.examples).length) return list(action.examples);
    return action.output || action.after ? [action] : [];
  }

  function imageFrame(src, alt, label, eager = true) {
    const figure = node('figure', 'stage-frame');
    if (!src) {
      figure.append(node('p', 'image-error', 'No image is attached to this view.'));
      return figure;
    }
    const img = node('img');
    img.src = src;
    img.alt = alt;
    img.decoding = 'async';
    img.loading = eager ? 'eager' : 'lazy';
    const setAspect = () => {
      if (img.naturalWidth && img.naturalHeight) figure.style.setProperty('--asset-ratio', `${img.naturalWidth} / ${img.naturalHeight}`);
    };
    img.addEventListener('load', setAspect, { once: true });
    if (img.complete) setAspect();
    img.addEventListener('error', () => {
      const message = node('p', 'image-error', 'This image could not be opened. Keep the gallery and its image folders together.');
      img.replaceWith(message);
    }, { once: true });
    figure.append(img, node('figcaption', 'frame-label', label));
    return figure;
  }

  function renderTabs() {
    const holder = $('action-tabs');
    holder.replaceChildren();
    actions.forEach((action, i) => {
      const button = node('button', 'action-tab');
      button.type = 'button';
      button.id = `action-tab-${i}`;
      button.setAttribute('role', 'tab');
      button.setAttribute('aria-controls', 'action-panel');
      button.setAttribute('aria-selected', String(i === activeIndex));
      button.tabIndex = i === activeIndex ? 0 : -1;
      button.append(node('span', 'tab-number', String(i + 1).padStart(2, '0')), node('span', 'tab-name', action.name || action.title || action.id), node('span', 'tab-arrow', '↗'));
      button.querySelector('.tab-arrow').setAttribute('aria-hidden', 'true');
      button.addEventListener('click', () => setAction(i, true));
      button.addEventListener('keydown', (event) => {
        let target = i;
        if (event.key === 'ArrowRight') target = (i + 1) % actions.length;
        else if (event.key === 'ArrowLeft') target = (i + actions.length - 1) % actions.length;
        else if (event.key === 'Home') target = 0;
        else if (event.key === 'End') target = actions.length - 1;
        else return;
        event.preventDefault();
        setAction(target, true);
      });
      holder.append(button);
    });
  }

  function setAction(index, focusTab) {
    if (index < 0 || index >= actions.length) return;
    activeIndex = index;
    exampleIndex = 0;
    view = 'output';
    renderTabs();
    renderAction();
    if (focusTab) $(`action-tab-${index}`).focus();
    text('announcement', `${actions[index].name || actions[index].id} selected. Result view.`);
    const hash = `#${actions[index].id || `action-${index + 1}`}`;
    try { history.replaceState(null, '', hash); } catch (_) { /* file contexts may prohibit state changes. */ }
  }

  function renderAction() {
    const action = actions[activeIndex];
    $('action-panel').setAttribute('aria-labelledby', `action-tab-${activeIndex}`);
    text('action-kicker', action.kicker || `LEGACYIFY ${action.name || action.id || ''}`.toUpperCase());
    text('action-headline', action.headline || action.title || action.name || 'Legacyify');
    text('action-summary', action.summary || action.description);
    text('action-status', action.status || 'Development demonstration');
    text('action-boundary', action.boundary || 'Inspect the source and its requirements before making a generation request. These demonstrations do not establish reliability for every input.');
    text('command-name', `Legacyify ${action.name || action.id}`);
    text('action-command', action.command || defaultCommands[action.id] || defaultCommands.scene);
    text('copy-feedback', '');
    $('copy-command').disabled = false;
    renderExampleRail();
    renderExample();
  }

  function renderExampleRail() {
    const action = actions[activeIndex];
    const items = examples(action);
    const holder = $('example-rail');
    holder.replaceChildren();
    holder.hidden = items.length < 2;
    items.forEach((example, i) => {
      const button = node('button', 'example-card');
      button.type = 'button';
      button.setAttribute('aria-pressed', String(i === exampleIndex));
      button.setAttribute('aria-label', `Show ${example.title || `example ${i + 1}`}`);
      const image = node('img');
      image.src = asset(example, 'output');
      image.alt = '';
      image.loading = 'lazy';
      image.addEventListener('error', () => { image.hidden = true; }, { once: true });
      const body = node('span', 'example-card-body');
      body.append(node('span', 'example-card-title', example.title || `Example ${i + 1}`), node('span', 'example-card-meta', example.outcome || example.status || example.attemptId || 'Development example'));
      button.append(image, body);
      button.addEventListener('click', () => {
        exampleIndex = i;
        view = 'output';
        renderExampleRail();
        renderExample();
        holder.children[i].focus();
        text('announcement', `${example.title || `Example ${i + 1}`} selected. Result view.`);
      });
      holder.append(button);
    });
  }

  function renderExample() {
    const action = actions[activeIndex];
    const items = examples(action);
    const example = items[exampleIndex];
    const stage = $('image-stage');
    stage.replaceChildren();
    stage.classList.toggle('is-compare', view === 'compare');
    if (!example) {
      text('example-count', '');
      text('example-title', 'No completed example attached');
      text('example-note', '');
      $('open-image').hidden = true;
      $('example-features').replaceChildren();
      $('extra-sources').hidden = true;
      stage.append(node('div', 'image-error', 'The campaign record has not attached a completed result to this action.'));
      document.querySelectorAll('[data-view]').forEach(button => { button.disabled = true; });
      return;
    }
    const source = asset(example, 'source');
    const output = asset(example, 'output');
    const sourceAlt = example.sourceAlt || example.beforeAlt || (typeof example.source === 'object' && example.source.alt) || `Source for ${example.title || action.name}`;
    const outputAlt = example.outputAlt || example.afterAlt || (typeof example.output === 'object' && example.output.alt) || `Legacyify result: ${example.title || action.name}`;
    if ((view === 'source' || view === 'compare') && !source) view = 'output';
    stage.classList.toggle('is-compare', view === 'compare');
    if (view === 'source' || view === 'compare') stage.append(imageFrame(source, sourceAlt, example.sourceLabel || 'Source'));
    if (view === 'output' || view === 'compare') stage.append(imageFrame(output, outputAlt, example.outputLabel || 'Legacyify result'));
    document.querySelectorAll('[data-view]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.view === view));
      button.disabled = button.dataset.view !== 'output' && !source;
    });
    text('example-count', `${String(exampleIndex + 1).padStart(2, '0')} / ${String(items.length).padStart(2, '0')}`);
    text('example-title', example.title || action.name || 'Demonstration');
    text('example-note', example.note || example.caption || '');
    $('open-image').href = view === 'source' ? source : output;
    $('open-image').hidden = !(view === 'source' ? source : output);
    const features = $('example-features');
    features.replaceChildren();
    list(example.features || action.features).forEach(feature => features.append(node('span', 'feature-tag', feature)));
    const extra = $('extra-sources');
    extra.replaceChildren();
    list(example.extraSources || action.extraSources).forEach(sourceItem => {
      const link = node('a', 'extra-source');
      link.href = path(sourceItem);
      link.target = '_blank';
      link.rel = 'noopener';
      const img = node('img');
      img.src = path(sourceItem);
      img.alt = sourceItem.alt || '';
      img.loading = 'lazy';
      link.append(img, node('span', '', sourceItem.label || 'Additional reference'));
      extra.append(link);
    });
    extra.hidden = !extra.children.length;
  }

  function renderWalkthrough() {
    text('campaign-note', data.note || 'These are development demonstrations. Each attempt retains its own record; a strong selected image is not a universal reliability claim.');
    const steps = list(data.walkthrough).length ? list(data.walkthrough) : [
      { title: 'Resolve the image and its references', text: 'The input supplies the task. Canonical character and logo masters control their assigned identities. Each reference has a separate role.' },
      { title: 'Set the boundary before generation', text: 'Identify what must stay correct, choose the visual medium, and define the allowed change. Then make one request for one output.' },
      { title: 'Inspect the result honestly', text: 'Compare source fidelity and standalone visual quality separately. Preserve every output and limitation before choosing the next development step.' }
    ];
    const holder = $('workflow-steps');
    steps.forEach((step, i) => {
      const article = node('article', 'workflow-step');
      article.append(node('span', 'workflow-step-number', String(i + 1).padStart(2, '0')), node('h3', '', step.title || `Step ${i + 1}`), node('p', '', step.text || step.description || ''));
      holder.append(article);
    });
    let attempts = list(data.attempts);
    if (!attempts.length) {
      attempts = actions.flatMap(action => examples(action).filter(example => example.attemptId || example.record).map(example => ({ id: example.attemptId || example.title, action: action.name || action.id, outcome: example.outcome || example.status || 'See record', note: example.note || '', record: example.record })));
      $('attempts-title').textContent = 'Demonstration records';
      document.querySelector('.record-context').textContent = 'These records belong to the displayed examples. Use the full ledger linked below for the complete campaign.';
    }
    $('attempts-section').hidden = !attempts.length;
    attempts.forEach(attempt => {
      const row = node('tr');
      [attempt.id || attempt.attemptId || '—', attempt.action || '—', attempt.outcome || attempt.status || '—', attempt.note || attempt.finding || '—'].forEach(value => row.append(node('td', '', value)));
      const cell = node('td');
      const href = path(attempt.record || attempt.href);
      if (href) {
        const link = node('a', '', 'Open record ↗');
        link.href = href;
        link.target = '_blank';
        link.rel = 'noopener';
        cell.append(link);
      } else cell.textContent = '—';
      row.append(cell);
      $('attempts-body').append(row);
    });
    list(data.records).forEach(record => {
      const link = node('a', '', `${record.label || record.title || 'Campaign record'} ↗`);
      link.href = path(record.href || record.path || record.url);
      link.target = '_blank';
      link.rel = 'noopener';
      $('record-links').append(link);
    });
    text('budget-note', data.budget);
  }

  document.querySelectorAll('[data-view]').forEach(button => button.addEventListener('click', () => {
    view = button.dataset.view;
    renderExample();
    text('announcement', view === 'compare' ? 'Source and result shown together.' : `${view === 'source' ? 'Source' : 'Result'} view selected.`);
  }));

  $('copy-command').addEventListener('click', async () => {
    clearTimeout(feedbackTimer);
    const command = $('action-command').textContent;
    let copied = false;
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(command);
        copied = true;
      }
    } catch (_) { /* Try the local-file-compatible selection path. */ }
    if (!copied) {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents($('action-command'));
      selection.removeAllRanges();
      selection.addRange(range);
      try { copied = document.execCommand('copy'); } catch (_) { copied = false; }
      if (copied) selection.removeAllRanges();
    }
    text('copy-feedback', copied ? 'Request copied. Attach your image in Codex, then paste it.' : 'Request selected. Press Ctrl+C (or ⌘C), then paste it in Codex with your image.');
    if (copied) feedbackTimer = setTimeout(() => text('copy-feedback', ''), 7000);
  });

  if (data.title) document.title = data.title;
  text('campaign-date', data.date || '');
  if (data.subtitle) text('gallery-subtitle', data.subtitle);
  if (!actions.length) {
    $('action-panel').replaceChildren(node('div', 'empty-state', 'No campaign images have been attached yet. Add the campaign data and keep the image folders beside this gallery.'));
    $('fresh-inputs').hidden = true;
    $('action-tabs').hidden = true;
  } else {
    let hashId = location.hash.slice(1);
    try { hashId = decodeURIComponent(hashId); } catch (_) { /* Ignore malformed optional deep links. */ }
    const hashIndex = actions.findIndex(action => action.id === hashId);
    if (hashIndex >= 0) activeIndex = hashIndex;
    renderTabs();
    renderAction();
  }
  renderWalkthrough();
  window.legacyGallery = Object.freeze({
    getState: () => ({ action: actions[activeIndex]?.id, example: exampleIndex, view, actionCount: actions.length }),
    showAction: (id) => { const i = actions.findIndex(action => action.id === id); if (i >= 0) setAction(i, false); }
  });
})();
