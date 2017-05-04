/**
 * Responds to any HTTP request that can provide a "message" field in the body.
 *
 * @param {!Object} req Cloud Function request context.
 * @param {!Object} res Cloud Function response context.
 */
exports.debateflowsapi = function debateflowsapi(req, res) {

  console.log("request")
  console.log(req);
  console.log(req.body.message);
  console.log(req.body)
  res.status(200).send('pong');
};
